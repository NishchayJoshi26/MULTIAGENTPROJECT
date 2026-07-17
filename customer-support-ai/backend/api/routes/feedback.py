from fastapi import APIRouter
from backend.schemas.common import EmptyResponse

router = APIRouter(prefix="/feedback", tags=["feedback"])


@router.get("", response_model=EmptyResponse)
def feedback_placeholder() -> EmptyResponse:
    return EmptyResponse(status="ok", message="Feedback routes placeholder")
