from pydantic import BaseModel
from typing import List, Optional
from app.schemas.strategy import StrategyResponse
from app.schemas.content import ContentResponse
from app.schemas.review import ReviewResponse


class MarketingFlowRequest(BaseModel):
    business_name: str
    audience: str
    platform: str


class CitationItem(BaseModel):
    chunk_id: str
    title: str
    source: str
    source_type: str
    platform: Optional[str] = None
    account_name: Optional[str] = None
    text: str


class MarketingFlowResponse(BaseModel):
    strategy: StrategyResponse
    content: ContentResponse
    review: ReviewResponse
    sources: List[CitationItem]
    orchestrator: str