def build_copywriter_prompts(
    business_name: str,
    audience: str,
    platform: str,
    tone: str | None = None,
    campaign_idea: str | None = None,
    context: str | None = None,
    improvements: list[str] | None = None,
):
    system_prompt = (
        "You are a senior marketing copywriter for small businesses. "
        "Write concise, catchy, platform-aware social media copy grounded in the provided business context."
    )

    user_prompt = f"""
Business name: {business_name}
Target audience: {audience}
Platform: {platform}
Tone: {tone or "Friendly and engaging"}
Campaign idea: {campaign_idea or "General brand awareness"}

Business context:
{context or "No additional context provided."}

Requirements:
- Write one strong social media post
- Make it natural and specific
- Use the business context when relevant
- Add one clear call to action
- Add 3-5 relevant hashtags
- Keep it suitable for the requested platform
""".strip()

    if improvements:
        user_prompt += "\n\nImprove based on the following feedback:\n"
        user_prompt += "\n".join(f"- {item}" for item in improvements)

    return system_prompt, user_prompt