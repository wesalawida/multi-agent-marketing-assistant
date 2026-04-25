from app.services.copywriter_service import generate_marketing_content
from app.schemas.content import ContentRequest, ContentResponse
from app.services.logging_service import log_agent_event


def run_copywriter_agent(
    data: ContentRequest,
    tone: str | None = None,
    campaign_idea: str | None = None,
    context: str | None = None,
    improvements: list[str] | None = None,
) -> ContentResponse:
    log_agent_event("CopywriterAgent", f"Generating content for {data.business_name}")

    content = generate_marketing_content(
        business_name=data.business_name,
        audience=data.audience,
        platform=data.platform,
        tone=tone,
        campaign_idea=campaign_idea,
        context=context,
        improvements=improvements,
    )

    log_agent_event("CopywriterAgent", "Content generation completed")

    return ContentResponse(
        platform=data.platform,
        content=content,
        agent="CopywriterAgent"
    )