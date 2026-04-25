from fastapi import APIRouter
from app.schemas.orchestrator import MarketingFlowRequest, MarketingFlowResponse
from app.agents.orchestrator_agent import run_marketing_flow

router = APIRouter()

@router.post("/run-marketing-flow", response_model=MarketingFlowResponse)
def run_marketing_flow_route(data: MarketingFlowRequest):
    return run_marketing_flow(data)