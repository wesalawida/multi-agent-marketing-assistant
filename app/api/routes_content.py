from fastapi import APIRouter
from app.schemas.content import ContentRequest, ContentResponse
from app.agents.copywriter_agent import run_copywriter_agent

router = APIRouter()


@router.post("/generate-content", response_model=ContentResponse)
def generate_content(data: ContentRequest):
    return run_copywriter_agent(data)