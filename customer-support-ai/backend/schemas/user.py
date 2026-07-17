from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserCreateSchema(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    role: str = "customer"


class UserUpdateSchema(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    avatar_url: Optional[str] = None
    is_active: Optional[bool] = None


class UserSchema(BaseModel):
    id: Optional[str] = None
    name: str
    email: EmailStr
    role: str = "customer"
    avatar_url: Optional[str] = None
    is_active: bool = True
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    is_deleted: bool = False
