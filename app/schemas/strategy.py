from pydantic import BaseModel
from typing import List


class StrategyRequest(BaseModel):
    business_name: str
    audience: str
    platform: str


class StrategyResponse(BaseModel):
    business_name: str
    pillars: List[str]
    tone: str
    campaign_idea: str
    agent: str