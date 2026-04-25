from app.services.llm_service import generate_llm_marketing_content


def generate_marketing_content(
    business_name: str,
    audience: str,
    platform: str,
    tone: str | None = None,
    campaign_idea: str | None = None,
    context: str | None = None,
    improvements: list[str] | None = None,
) -> str:
    return generate_llm_marketing_content(
        business_name=business_name,
        audience=audience,
        platform=platform,
        tone=tone,
        campaign_idea=campaign_idea,
        context=context,
        improvements=improvements,
    )