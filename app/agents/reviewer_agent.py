import json
from app.schemas.review import ReviewRequest, ReviewResponse
from app.services.reviewer_service import review_marketing_content


def run_reviewer_agent(data: ReviewRequest) -> ReviewResponse:
    result = review_marketing_content(
        business_name=data.business_name,
        platform=data.platform,
        content=data.content,
    )

    raw_output = result["raw_output"]

    try:
        parsed = json.loads(raw_output)
    except Exception:
        # fallback אם המודל לא החזיר JSON
        parsed = {
            "score": 5,
            "strengths": ["Model output not structured properly"],
            "improvements": ["Retry generation", "Improve prompt"],
            "approved": False
        }

    return ReviewResponse(
        score=parsed.get("score", 5),
        strengths=parsed.get("strengths", []),
        improvements=parsed.get("improvements", []),
        approved=parsed.get("approved", False),
        agent="ReviewerAgent",
    )