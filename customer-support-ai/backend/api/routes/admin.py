from fastapi import APIRouter
from backend.schemas.common import EmptyResponse

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("", response_model=EmptyResponse)
def admin_placeholder() -> EmptyResponse:
    return EmptyResponse(status="ok", message="Admin routes placeholder")
