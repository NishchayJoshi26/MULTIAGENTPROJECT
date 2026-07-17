from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Any, Optional

from backend.models.session import Session
from backend.repositories.base_repository import BaseRepository


class SessionRepository(BaseRepository):
    def __init__(self, collection: Any) -> None:
        super().__init__(collection)

    async def create(self, session: Session) -> Session:
        session.id = session.id or str(uuid.uuid4())
        session.created_at = session.created_at or datetime.now(timezone.utc)
        session.updated_at = session.updated_at or datetime.now(timezone.utc)
        document = session.model_dump(exclude_none=True)
        result = await self.collection.insert_one(document)
        inserted_id = getattr(result, "inserted_id", None)
        if inserted_id is not None:
            session.id = str(inserted_id)
        return session

    async def get_by_id(self, document_id: str) -> Optional[Session]:
        document = await self.collection.find_one({"_id": document_id})
        if not document or document.get("is_deleted"):
            return None
        payload = dict(document)
        payload["id"] = payload.get("_id")
        return Session(**payload)

    async def update(self, document_id: str, values: dict) -> Optional[Session]:
        await self.collection.update_one({"_id": document_id}, {"$set": values})
        return await self.get_by_id(document_id)

    async def delete(self, document_id: str) -> bool:
        result = await self.collection.delete_one({"_id": document_id})
        return result.deleted_count > 0

    async def soft_delete(self, document_id: str) -> Optional[Session]:
        await self.collection.update_one({"_id": document_id}, {"$set": {"is_deleted": True, "updated_at": datetime.now(timezone.utc)}})
        return await self.get_by_id(document_id)

    async def restore(self, document_id: str) -> Optional[Session]:
        await self.collection.update_one({"_id": document_id}, {"$set": {"is_deleted": False, "updated_at": datetime.now(timezone.utc)}})
        document = await self.collection.find_one({"_id": document_id})
        if not document:
            return None
        return Session(**document)

    async def create_indexes(self) -> None:
        await self.collection.create_index([("user_id", 1)])
        await self.collection.create_index([("is_deleted", 1)])
