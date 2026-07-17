from __future__ import annotations

from typing import Any

from backend.database.connection import DatabaseConnection
from backend.repositories.analytics_repository import AnalyticsRepository
from backend.repositories.chat_repository import ChatRepository
from backend.repositories.document_repository import DocumentRepository
from backend.repositories.feedback_repository import FeedbackRepository
from backend.repositories.message_repository import MessageRepository
from backend.repositories.session_repository import SessionRepository
from backend.repositories.ticket_repository import TicketRepository
from backend.repositories.user_repository import UserRepository


class DatabaseService:
    def __init__(self, database: Any | None = None) -> None:
        self.database = database or DatabaseConnection.get_db()
        self.users = UserRepository(self.database.users)
        self.chats = ChatRepository(self.database.chats)
        self.messages = MessageRepository(self.database.messages)
        self.sessions = SessionRepository(self.database.sessions)
        self.feedback = FeedbackRepository(self.database.feedback)
        self.tickets = TicketRepository(self.database.tickets)
        self.analytics = AnalyticsRepository(self.database.analytics)
        self.documents = DocumentRepository(self.database.documents)

    async def initialize(self) -> None:
        await self.users.create_indexes()
        await self.chats.create_indexes()
        await self.messages.create_indexes()
        await self.sessions.create_indexes()
        await self.feedback.create_indexes()
        await self.tickets.create_indexes()
        await self.analytics.create_indexes()
        await self.documents.create_indexes()
