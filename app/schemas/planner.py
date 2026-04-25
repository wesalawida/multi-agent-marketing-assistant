from pydantic import BaseModel
from typing import List


class PlannerRequest(BaseModel):
    business_name: str
    audience: str
    platform: str


class PlannerResponse(BaseModel):
    business_name: str
    weekly_plan: List[str]
    agent: str