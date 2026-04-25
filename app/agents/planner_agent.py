from app.schemas.planner import PlannerRequest, PlannerResponse
from app.services.planner_service import generate_weekly_plan


def run_planner_agent(data: PlannerRequest) -> PlannerResponse:
    weekly_plan = generate_weekly_plan(
        business_name=data.business_name,
        audience=data.audience,
        platform=data.platform
    )

    return PlannerResponse(
        business_name=data.business_name,
        weekly_plan=weekly_plan,
        agent="PlannerAgent"
    )