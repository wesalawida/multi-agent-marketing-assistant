from fastapi import APIRouter
from app.schemas.strategy import StrategyRequest, StrategyResponse
from app.agents.strategy_agent import run_strategy_agent

router = APIRouter()

@router.post("/generate-strategy", response_model=StrategyResponse)
def generate_strategy(data: StrategyRequest):
    return run_strategy_agent(data)