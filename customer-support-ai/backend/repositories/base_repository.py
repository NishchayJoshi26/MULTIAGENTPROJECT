from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional


class BaseRepository(ABC):
    def __init__(self, collection: Any) -> None:
        self.collection = collection

    @abstractmethod
    async def create(self, document: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, document_id: str) -> Optional[Any]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, document_id: str, values: dict) -> Optional[Any]:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, document_id: str) -> bool:
        raise NotImplementedError
