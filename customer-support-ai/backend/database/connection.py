from motor.motor_asyncio import AsyncIOMotorClient
from backend.config.settings import settings


class DatabaseConnection:
    client: AsyncIOMotorClient | None = None

    @classmethod
    async def connect(cls) -> None:
        if cls.client is None:
            cls.client = AsyncIOMotorClient(settings.mongodb_uri)

    @classmethod
    async def disconnect(cls) -> None:
        if cls.client is not None:
            cls.client.close()
            cls.client = None

    @classmethod
    def get_db(cls):
        if cls.client is None:
            raise RuntimeError("Database not connected")
        return cls.client[settings.mongodb_db_name]
