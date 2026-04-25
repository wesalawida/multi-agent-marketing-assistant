from app.schemas.orchestrator import MarketingFlowRequest, MarketingFlowResponse, CitationItem
from app.schemas.strategy import StrategyRequest
from app.schemas.content import ContentRequest
from app.schemas.review import ReviewRequest
from app.agents.strategy_agent import run_strategy_agent
from app.agents.copywriter_agent import run_copywriter_agent
from app.agents.reviewer_agent import run_reviewer_agent
from app.rag.retriever import (
    get_context_for_business,
    get_inspiration_context,
    get_brand_chunks,
    get_inspiration_chunks,
)


def run_marketing_flow(data: MarketingFlowRequest) -> MarketingFlowResponse:
    # 1. Strategy
    strategy_input = StrategyRequest(
        business_name=data.business_name,
        audience=data.audience,
        platform=data.platform
    )
    strategy_result = run_strategy_agent(strategy_input)

    # 2. Build content input
    content_input = ContentRequest(
        business_name=data.business_name,
        audience=data.audience,
        platform=data.platform
    )

    # 3. Collect RAG context
    brand_context = get_context_for_business(data.business_name)
    inspiration_context = get_inspiration_context(
        query=data.audience,
        platform=data.platform
    )

    combined_context = f"""
BRAND CONTEXT:
{brand_context}

INSPIRATION CONTEXT:
{inspiration_context}
""".strip()

    # 4. First content generation
    content_result = run_copywriter_agent(
        content_input,
        tone=strategy_result.tone,
        campaign_idea=strategy_result.campaign_idea,
        context=combined_context,
    )

    # 5. Review the generated content
    review_input = ReviewRequest(
        business_name=data.business_name,
        platform=data.platform,
        content=content_result.content,
    )
    review_result = run_reviewer_agent(review_input)

    # 6. Auto-improvement loop: if not approved, regenerate once using reviewer feedback
    if not review_result.approved:
        improved_content = run_copywriter_agent(
            content_input,
            tone=strategy_result.tone,
            campaign_idea=strategy_result.campaign_idea,
            context=combined_context,
            improvements=review_result.improvements,
        )

        improved_review_input = ReviewRequest(
            business_name=data.business_name,
            platform=data.platform,
            content=improved_content.content,
        )
        improved_review_result = run_reviewer_agent(improved_review_input)

        content_result = improved_content
        review_result = improved_review_result

    # 7. Gather citations / sources
    brand_chunks = get_brand_chunks(data.business_name)
    inspiration_chunks = get_inspiration_chunks(
        data.audience,
        platform=data.platform
    )

    all_chunks = brand_chunks + inspiration_chunks

    seen = set()
    unique_chunks = []

    for item in all_chunks:
        key = (item["chunk_id"], item["title"], item["source"])
        if key not in seen:
            seen.add(key)
            unique_chunks.append(item)

    sources = [
        CitationItem(
            chunk_id=item["chunk_id"],
            title=item["title"],
            source=item["source"],
            source_type=item["source_type"],
            platform=item.get("platform"),
            account_name=item.get("account_name"),
            text=item["text"],
        )
        for item in unique_chunks
    ]

    # 8. Final response
    return MarketingFlowResponse(
        strategy=strategy_result,
        content=content_result,
        review=review_result,
        sources=sources,
        orchestrator="MarketingOrchestrator"
    )