from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Any, Optional

from backend.models.user import User
from backend.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, collection: Any) -> None:
        super().__init__(collection)

    async def create(self, user: User) -> User:
        user.id = user.id or str(uuid.uuid4())
        user.created_at = user.created_at or datetime.now(timezone.utc)
        user.updated_at = user.updated_at or datetime.now(timezone.utc)
        document = user.model_dump(exclude_none=True)
        result = await self.collection.insert_one(document)
        inserted_id = getattr(result, "inserted_id", None)
        if inserted_id is not None:
            user.id = str(inserted_id)
        return user

    async def get_by_id(self, document_id: str) -> Optional[User]:
        document = await self.collection.find_one({"_id": document_id})
        if not document or document.get("is_deleted"):
            return None
        payload = dict(document)
        payload["id"] = payload.get("_id")
        return User(**payload)

    async def get_by_email(self, email: str) -> Optional[User]:
        document = await self.collection.find_one({"email": email})
        if not document or document.get("is_deleted"):
            return None
        return User(**document)

    async def update(self, document_id: str, values: dict) -> Optional[User]:
        await self.collection.update_one({"_id": document_id}, {"$set": values})
        return await self.get_by_id(document_id)

    async def delete(self, document_id: str) -> bool:
        result = await self.collection.delete_one({"_id": document_id})
        return result.deleted_count > 0

    async def soft_delete(self, document_id: str) -> Optional[User]:
        await self.collection.update_one({"_id": document_id}, {"$set": {"is_deleted": True, "updated_at": datetime.now(timezone.utc)}})
        document = await self.collection.find_one({"_id": document_id})
        if not document:
            return None
        return User(**document)

    async def restore(self, document_id: str) -> Optional[User]:
        await self.collection.update_one({"_id": document_id}, {"$set": {"is_deleted": False, "updated_at": datetime.now(timezone.utc)}})
        document = await self.collection.find_one({"_id": document_id})
        if not document:
            return None
        return User(**document)

    async def create_indexes(self) -> None:
        await self.collection.create_index([("email", 1)], unique=True)
        await self.collection.create_index([("is_deleted", 1)])
