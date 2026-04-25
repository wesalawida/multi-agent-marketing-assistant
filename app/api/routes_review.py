from fastapi import APIRouter
from app.schemas.review import ReviewRequest, ReviewResponse
from app.agents.reviewer_agent import run_reviewer_agent

router = APIRouter()


@router.post("/review-content", response_model=ReviewResponse)
def review_content(data: ReviewRequest):
    return run_reviewer_agent(data)