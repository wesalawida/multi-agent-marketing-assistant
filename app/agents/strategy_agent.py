from app.schemas.strategy import StrategyRequest, StrategyResponse
from app.services.strategy_service import generate_strategy


def run_strategy_agent(data: StrategyRequest) -> StrategyResponse:
    strategy = generate_strategy(
        business_name=data.business_name,
        audience=data.audience,
        platform=data.platform
    )

    return StrategyResponse(
        business_name=data.business_name,
        pillars=strategy["pillars"],
        tone=strategy["tone"],
        campaign_idea=strategy["campaign_idea"],
        agent="StrategyAgent"
    )