from fastapi import FastAPI
from app.api.routes_content import router as content_router
from app.api.routes_strategy import router as strategy_router
from app.api.routes_orchestrator import router as orchestrator_router
from app.api.routes_planner import router as planner_router
from app.api.routes_rag import router as rag_router
from app.api.routes_inspiration import router as inspiration_router
from app.api.routes_connectors import router as connectors_router
from app.api.routes_review import router as review_router

app = FastAPI(title="Multi-Agent Marketing Assistant API")

@app.get("/")
def read_root():
    return {"message": "Multi-Agent Marketing Assistant is running!"}

app.include_router(content_router, tags=["Content"])
app.include_router(strategy_router, tags=["Strategy"])
app.include_router(orchestrator_router, tags=["Orchestrator"])
app.include_router(planner_router, tags=["Planner"])
app.include_router(rag_router, tags=["RAG"])
app.include_router(inspiration_router, tags=["Inspiration"])
app.include_router(connectors_router, tags=["Connectors"])
app.include_router(review_router, tags=["Review"])