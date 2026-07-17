from typing import Any, Optional

from motor.motor_asyncio import AsyncIOMotorClient

from backend.config.settings import settings


class DatabaseConnection:
    client: Optional[AsyncIOMotorClient] = None
    db: Optional[Any] = None

    @classmethod
    async def connect(cls) -> Any:
        if cls.client is None:
            cls.client = AsyncIOMotorClient(settings.mongodb_uri)
            cls.db = cls.client[settings.mongodb_db_name]
        return cls.db

    @classmethod
    async def disconnect(cls) -> None:
        if cls.client is not None:
            cls.client.close()
            cls.client = None
            cls.db = None

    @classmethod
    def get_db(cls) -> Any:
        if cls.client is None:
            raise RuntimeError("Database not connected")
        if cls.db is None:
            cls.db = cls.client[settings.mongodb_db_name]
        return cls.db

    @classmethod
    def get_collection(cls, name: str) -> Any:
        return cls.get_db()[name]
