from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Any, Optional

from backend.models.feedback import Feedback
from backend.repositories.base_repository import BaseRepository


class FeedbackRepository(BaseRepository):
    def __init__(self, collection: Any) -> None:
        super().__init__(collection)

    async def create(self, feedback: Feedback) -> Feedback:
        feedback.id = feedback.id or str(uuid.uuid4())
        feedback.created_at = feedback.created_at or datetime.now(timezone.utc)
        feedback.updated_at = feedback.updated_at or datetime.now(timezone.utc)
        document = feedback.model_dump(exclude_none=True)
        result = await self.collection.insert_one(document)
        inserted_id = getattr(result, "inserted_id", None)
        if inserted_id is not None:
            feedback.id = str(inserted_id)
        return feedback

    async def get_by_id(self, document_id: str) -> Optional[Feedback]:
        document = await self.collection.find_one({"_id": document_id})
        if not document or document.get("is_deleted"):
            return None
        payload = dict(document)
        payload["id"] = payload.get("_id")
        return Feedback(**payload)

    async def update(self, document_id: str, values: dict) -> Optional[Feedback]:
        await self.collection.update_one({"_id": document_id}, {"$set": values})
        return await self.get_by_id(document_id)

    async def delete(self, document_id: str) -> bool:
        result = await self.collection.delete_one({"_id": document_id})
        return result.deleted_count > 0

    async def soft_delete(self, document_id: str) -> Optional[Feedback]:
        await self.collection.update_one({"_id": document_id}, {"$set": {"is_deleted": True, "updated_at": datetime.now(timezone.utc)}})
        return await self.get_by_id(document_id)

    async def restore(self, document_id: str) -> Optional[Feedback]:
        await self.collection.update_one({"_id": document_id}, {"$set": {"is_deleted": False, "updated_at": datetime.now(timezone.utc)}})
        document = await self.collection.find_one({"_id": document_id})
        if not document:
            return None
        return Feedback(**document)

    async def create_indexes(self) -> None:
        await self.collection.create_index([("ticket_id", 1)])
        await self.collection.create_index([("is_deleted", 1)])
