import secrets
from datetime import datetime, timedelta, timezone
from typing import Dict, Optional, Tuple

import bcrypt
import jwt
from fastapi import HTTPException, status

from backend.config.settings import settings
from backend.models.user import User
from backend.repositories.user_repository import UserRepository
from backend.schemas.auth import TokenResponse, UserLoginRequest, UserRegisterRequest, UserResponse


class _InMemoryCollection:
    def __init__(self) -> None:
        self.documents = []

    async def insert_one(self, document):
        document = dict(document)
        document["_id"] = str(len(self.documents) + 1)
        self.documents.append(document)
        return type("Result", (), {"inserted_id": document["_id"]})()

    async def find_one(self, filter_query):
        for document in self.documents:
            if all(document.get(key) == value for key, value in filter_query.items()):
                return document
        return None

    async def update_one(self, filter_query, update):
        for index, document in enumerate(self.documents):
            if all(document.get(key) == value for key, value in filter_query.items()):
                new_doc = dict(document)
                for key, value in update.get("$set", {}).items():
                    new_doc[key] = value
                self.documents[index] = new_doc
                return type("Result", (), {"matched_count": 1})()
        return type("Result", (), {"matched_count": 0})()

    async def delete_one(self, filter_query):
        for index, document in enumerate(self.documents):
            if all(document.get(key) == value for key, value in filter_query.items()):
                del self.documents[index]
                return type("Result", (), {"deleted_count": 1})()
        return type("Result", (), {"deleted_count": 0})()

    async def create_index(self, keys, unique=False):
        return "index"


class AuthService:
    _refresh_tokens: Dict[str, str] = {}

    def __init__(self, repository: Optional[UserRepository] = None) -> None:
        self.repository = repository or self._build_default_repository()

    def _build_default_repository(self) -> UserRepository:
        return UserRepository(collection=_InMemoryCollection())

    async def register(self, request: UserRegisterRequest) -> Tuple[UserResponse, TokenResponse]:
        email = str(request.email).lower()
        existing = await self.repository.get_by_email(email)
        if existing is not None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

        password_hash = self._hash_password(request.password)
        user = User(
            id=f"user_{secrets.token_hex(4)}",
            name=request.name,
            email=request.email,
            password_hash=password_hash,
            role=request.role,
        )
        await self.repository.create(user)
        tokens = self._issue_tokens(user)
        return self._to_user_response(user), tokens

    async def login(self, request: UserLoginRequest) -> Tuple[UserResponse, TokenResponse]:
        email = str(request.email).lower()
        user = await self.repository.get_by_email(email)
        if not user or not self._verify_password(request.password, user.password_hash):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        tokens = self._issue_tokens(user)
        return self._to_user_response(user), tokens

    async def logout(self, refresh_token: str) -> None:
        if refresh_token in self._refresh_tokens:
            self._refresh_tokens.pop(refresh_token, None)

    async def refresh(self, refresh_token: str) -> TokenResponse:
        user_id = self._decode_token(refresh_token, expected_type="refresh")
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
        user = await self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return self._issue_tokens(user)

    async def get_me(self, token: str) -> UserResponse:
        user_id = self._decode_token(token, expected_type="access")
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid access token")
        user = await self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return self._to_user_response(user)

    def _issue_tokens(self, user: User) -> TokenResponse:
        access_payload = {"sub": user.id, "role": user.role, "type": "access", "exp": datetime.now(timezone.utc) + timedelta(minutes=15)}
        refresh_payload = {"sub": user.id, "role": user.role, "type": "refresh", "exp": datetime.now(timezone.utc) + timedelta(days=7)}
        access_token = jwt.encode(access_payload, settings.jwt_secret, algorithm="HS256")
        refresh_token = jwt.encode(refresh_payload, settings.jwt_refresh_secret, algorithm="HS256")
        self._refresh_tokens[refresh_token] = user.id
        return TokenResponse(access_token=access_token, refresh_token=refresh_token)

    def _decode_token(self, token: str, expected_type: str) -> Optional[str]:
        try:
            payload = jwt.decode(token, settings.jwt_secret if expected_type == "access" else settings.jwt_refresh_secret, algorithms=["HS256"])
        except jwt.PyJWTError:
            return None
        if payload.get("type") != expected_type:
            return None
        return payload.get("sub")

    def _hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt(rounds=12)
        return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")

    def _verify_password(self, password: str, password_hash: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8"))

    def _to_user_response(self, user: User) -> UserResponse:
        return UserResponse(id=user.id, name=user.name, email=user.email, role=user.role, avatar_url=user.avatar_url, is_active=user.is_active)
