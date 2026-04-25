from fastapi import APIRouter
from app.schemas.planner import PlannerRequest, PlannerResponse
from app.agents.planner_agent import run_planner_agent

router = APIRouter()

@router.post("/generate-weekly-plan", response_model=PlannerResponse)
def generate_weekly_plan(data: PlannerRequest):
    return run_planner_agent(data)