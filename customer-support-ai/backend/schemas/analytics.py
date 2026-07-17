from __future__ import annotations

from typing import Optional
from pydantic import BaseModel


class AnalyticsCreateSchema(BaseModel):
    metric_name: str
    metric_value: float
    dimension: Optional[str] = None


class AnalyticsUpdateSchema(BaseModel):
    metric_value: Optional[float] = None
    dimension: Optional[str] = None


class AnalyticsSchema(BaseModel):
    id: Optional[str] = None
    metric_name: str
    metric_value: float
    dimension: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    is_deleted: bool = False
