import os
from dotenv import load_dotenv
from openai import OpenAI
from app.services.prompt_builder import build_copywriter_prompts

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def generate_llm_marketing_content(
    business_name: str,
    audience: str,
    platform: str,
    tone: str | None = None,
    campaign_idea: str | None = None,
    context: str | None = None,
    improvements: list[str] | None = None,
) -> str:
    system_prompt, user_prompt = build_copywriter_prompts(
        business_name=business_name,
        audience=audience,
        platform=platform,
        tone=tone,
        campaign_idea=campaign_idea,
        context=context,
        improvements=improvements,
    )

    response = client.responses.create(
        model=MODEL_NAME,
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    return response.output_text.strip()