from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field


class Ticket(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    subject: str
    content: str
    status: str = "open"
    priority: str = "medium"
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_deleted: bool = False
