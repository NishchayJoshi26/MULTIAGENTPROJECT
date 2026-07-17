from typing import Optional, Tuple

from fastapi import APIRouter, Depends, HTTPException, status

from backend.api.dependencies.auth import get_auth_context
from backend.schemas.auth import TokenResponse, UserLoginRequest, UserRegisterRequest, UserResponse
from backend.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])
service = AuthService()


@router.post("/register", response_model=Tuple[UserResponse, TokenResponse], status_code=status.HTTP_201_CREATED)
async def register(request: UserRegisterRequest) -> Tuple[UserResponse, TokenResponse]:
    return await service.register(request)


@router.post("/login", response_model=Tuple[UserResponse, TokenResponse])
async def login(request: UserLoginRequest) -> Tuple[UserResponse, TokenResponse]:
    return await service.login(request)


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(refresh_token: str) -> None:
    await service.logout(refresh_token)


@router.post("/refresh", response_model=TokenResponse)
async def refresh(refresh_token: str) -> TokenResponse:
    return await service.refresh(refresh_token)


@router.get("/me", response_model=UserResponse)
async def me(auth_context: Optional[dict[str, str]] = Depends(get_auth_context)) -> UserResponse:
    if auth_context is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")
    token = auth_context.get("token", "")
    return await service.get_me(token)
