from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class MessageCreateSchema(BaseModel):
    chat_id: str
    session_id: Optional[str] = None
    sender: str = "user"
    role: str = "user"
    content: str = Field(min_length=1)
    metadata: Optional[dict] = None


class MessageUpdateSchema(BaseModel):
    content: Optional[str] = None
    metadata: Optional[dict] = None


class MessageSchema(BaseModel):
    id: Optional[str] = None
    chat_id: str
    session_id: Optional[str] = None
    sender: str = "user"
    role: str = "user"
    content: str
    metadata: Optional[dict] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    is_deleted: bool = False
