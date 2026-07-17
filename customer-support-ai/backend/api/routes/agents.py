from fastapi import APIRouter
from pydantic import BaseModel, Field

from backend.agents.workflow import workflow

router = APIRouter(prefix="/agents", tags=["agents"])


class AgentRouteRequest(BaseModel):
    query: str = Field(..., min_length=1)


@router.post("/route", response_model=dict)
def route_query(payload: AgentRouteRequest) -> dict:
    return workflow.run(payload.query)
