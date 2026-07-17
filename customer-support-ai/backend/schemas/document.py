from __future__ import annotations

from typing import Optional
from pydantic import BaseModel


class DocumentCreateSchema(BaseModel):
    title: str
    content: Optional[str] = None
    source: Optional[str] = None
    metadata: Optional[dict] = None


class DocumentUpdateSchema(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    source: Optional[str] = None
    metadata: Optional[dict] = None


class DocumentSchema(BaseModel):
    id: Optional[str] = None
    title: str
    content: Optional[str] = None
    source: Optional[str] = None
    metadata: Optional[dict] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    is_deleted: bool = False
