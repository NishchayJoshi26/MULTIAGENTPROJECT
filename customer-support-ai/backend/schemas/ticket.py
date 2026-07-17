from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class TicketCreateSchema(BaseModel):
    user_id: Optional[str] = None
    subject: str = Field(min_length=2)
    content: str = Field(min_length=1)
    status: str = "open"
    priority: str = "medium"


class TicketUpdateSchema(BaseModel):
    subject: Optional[str] = None
    content: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None


class TicketSchema(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    subject: str
    content: str
    status: str = "open"
    priority: str = "medium"
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    is_deleted: bool = False
