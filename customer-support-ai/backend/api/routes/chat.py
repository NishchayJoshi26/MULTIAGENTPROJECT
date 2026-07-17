from fastapi import APIRouter
from backend.schemas.common import EmptyResponse

router = APIRouter(prefix="/chat", tags=["chat"])


@router.get("", response_model=EmptyResponse)
def chat_placeholder() -> EmptyResponse:
    return EmptyResponse(status="ok", message="Chat routes placeholder")
