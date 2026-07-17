from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class ChatCreateSchema(BaseModel):
    user_id: str
    session_id: Optional[str] = None
    title: Optional[str] = None
    status: str = "active"


class ChatUpdateSchema(BaseModel):
    title: Optional[str] = None
    status: Optional[str] = None


class ChatSchema(BaseModel):
    id: Optional[str] = None
    user_id: str
    session_id: Optional[str] = None
    title: Optional[str] = None
    status: str = "active"
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    is_deleted: bool = False
