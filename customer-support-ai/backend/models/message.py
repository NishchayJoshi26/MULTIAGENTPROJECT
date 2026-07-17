from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field


class Message(BaseModel):
    id: Optional[str] = None
    chat_id: str
    session_id: Optional[str] = None
    sender: str = "user"
    role: str = "user"
    content: str
    metadata: Optional[dict] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_deleted: bool = False
