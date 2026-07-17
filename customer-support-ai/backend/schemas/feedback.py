from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class FeedbackCreateSchema(BaseModel):
    user_id: Optional[str] = None
    ticket_id: Optional[str] = None
    rating: int = Field(default=5, ge=1, le=5)
    comment: Optional[str] = None


class FeedbackUpdateSchema(BaseModel):
    rating: Optional[int] = Field(default=None, ge=1, le=5)
    comment: Optional[str] = None


class FeedbackSchema(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    ticket_id: Optional[str] = None
    rating: int = Field(default=5, ge=1, le=5)
    comment: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    is_deleted: bool = False
