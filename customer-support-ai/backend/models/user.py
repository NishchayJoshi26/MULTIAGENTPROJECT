from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: Optional[str] = Field(default=None)
    name: str
    email: EmailStr
    password_hash: str
    role: str = "customer"
    avatar_url: Optional[str] = None
    is_active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    is_deleted: bool = False
