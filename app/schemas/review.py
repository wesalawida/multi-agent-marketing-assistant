from pydantic import BaseModel
from typing import List


class ReviewRequest(BaseModel):
    business_name: str
    platform: str
    content: str


class ReviewResponse(BaseModel):
    score: int
    strengths: List[str]
    improvements: List[str]
    approved: bool
    agent: str