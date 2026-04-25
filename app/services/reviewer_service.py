from app.services.llm_service import client, MODEL_NAME


def review_marketing_content(business_name: str, platform: str, content: str) -> dict:
    system_prompt = (
        "You are a senior marketing reviewer. "
        "You MUST return only valid JSON."
    )

    user_prompt = f"""
Business name: {business_name}
Platform: {platform}

Content:
{content}

Return ONLY JSON in this format:
{{
  "score": number,
  "strengths": ["..."],
  "improvements": ["..."],
  "approved": true/false
}}

Do not add any explanation.
"""

    response = client.responses.create(
        model=MODEL_NAME,
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    return {"raw_output": response.output_text.strip()}