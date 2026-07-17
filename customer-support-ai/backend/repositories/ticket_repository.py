from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Any, Optional

from backend.models.ticket import Ticket
from backend.repositories.base_repository import BaseRepository


class TicketRepository(BaseRepository):
    def __init__(self, collection: Any) -> None:
        super().__init__(collection)

    async def create(self, ticket: Ticket) -> Ticket:
        ticket.id = ticket.id or str(uuid.uuid4())
        ticket.created_at = ticket.created_at or datetime.now(timezone.utc)
        ticket.updated_at = ticket.updated_at or datetime.now(timezone.utc)
        document = ticket.model_dump(exclude_none=True)
        result = await self.collection.insert_one(document)
        inserted_id = getattr(result, "inserted_id", None)
        if inserted_id is not None:
            ticket.id = str(inserted_id)
        return ticket

    async def get_by_id(self, document_id: str) -> Optional[Ticket]:
        document = await self.collection.find_one({"_id": document_id})
        if not document or document.get("is_deleted"):
            return None
        payload = dict(document)
        payload["id"] = payload.get("_id")
        return Ticket(**payload)

    async def update(self, document_id: str, values: dict) -> Optional[Ticket]:
        await self.collection.update_one({"_id": document_id}, {"$set": values})
        return await self.get_by_id(document_id)

    async def delete(self, document_id: str) -> bool:
        result = await self.collection.delete_one({"_id": document_id})
        return result.deleted_count > 0

    async def soft_delete(self, document_id: str) -> Optional[Ticket]:
        await self.collection.update_one({"_id": document_id}, {"$set": {"is_deleted": True, "updated_at": datetime.now(timezone.utc)}})
        document = await self.collection.find_one({"_id": document_id})
        if not document:
            return None
        return Ticket(**document)

    async def restore(self, document_id: str) -> Optional[Ticket]:
        await self.collection.update_one({"_id": document_id}, {"$set": {"is_deleted": False, "updated_at": datetime.now(timezone.utc)}})
        document = await self.collection.find_one({"_id": document_id})
        if not document:
            return None
        return Ticket(**document)

    async def create_indexes(self) -> None:
        await self.collection.create_index([("status", 1)])
        await self.collection.create_index([("is_deleted", 1)])
