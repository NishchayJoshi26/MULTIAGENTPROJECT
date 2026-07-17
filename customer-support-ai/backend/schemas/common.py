from typing import Optional
from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(default="ok")
    service: str = Field(default="TechMart Support AI")
    environment: str = Field(default="development")


class EmptyResponse(BaseModel):
    status: str = Field(default="ok")
    message: str = Field(default="Placeholder response")


class PaginationResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: list[dict]


class DeleteResponse(BaseModel):
    deleted: bool
    id: str
    message: Optional[str] = None
