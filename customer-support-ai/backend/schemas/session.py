from __future__ import annotations

from typing import Optional
from pydantic import BaseModel


class SessionCreateSchema(BaseModel):
    user_id: str
    title: Optional[str] = None
    status: str = "active"


class SessionUpdateSchema(BaseModel):
    title: Optional[str] = None
    status: Optional[str] = None


class SessionSchema(BaseModel):
    id: Optional[str] = None
    user_id: str
    title: Optional[str] = None
    status: str = "active"
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    is_deleted: bool = False
