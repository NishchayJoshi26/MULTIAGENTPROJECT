from fastapi import APIRouter
from backend.schemas.common import EmptyResponse

router = APIRouter(prefix="/knowledge", tags=["knowledge"])


@router.get("", response_model=EmptyResponse)
def knowledge_placeholder() -> EmptyResponse:
    return EmptyResponse(status="ok", message="Knowledge routes placeholder")
