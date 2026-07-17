import asyncio
from datetime import datetime, timezone

import pytest

from backend.models.chat import Chat
from backend.models.ticket import Ticket
from backend.models.user import User
from backend.repositories.user_repository import UserRepository
from backend.repositories.chat_repository import ChatRepository
from backend.repositories.ticket_repository import TicketRepository


class FakeCollection:
    def __init__(self) -> None:
        self.documents = []
        self.indexes = []

    async def insert_one(self, document):
        document = dict(document)
        document["_id"] = str(len(self.documents) + 1)
        self.documents.append(document)
        return type("Result", (), {"inserted_id": document["_id"]})()

    async def find_one(self, filter_query):
        for document in self.documents:
            if all(document.get(key) == value for key, value in filter_query.items()):
                return document
        return None

    async def find(self, filter_query=None):
        filter_query = filter_query or {}
        items = [doc for doc in self.documents if all(doc.get(key) == value for key, value in filter_query.items())]
        return items

    async def update_one(self, filter_query, update):
        for index, document in enumerate(self.documents):
            if all(document.get(key) == value for key, value in filter_query.items()):
                new_doc = dict(document)
                for key, value in update.get("$set", {}).items():
                    new_doc[key] = value
                self.documents[index] = new_doc
                return type("Result", (), {"matched_count": 1})()
        return type("Result", (), {"matched_count": 0})()

    async def delete_one(self, filter_query):
        for index, document in enumerate(self.documents):
            if all(document.get(key) == value for key, value in filter_query.items()):
                del self.documents[index]
                return type("Result", (), {"deleted_count": 1})()
        return type("Result", (), {"deleted_count": 0})()

    async def create_index(self, keys, unique=False):
        self.indexes.append((keys, unique))
        return "index"


@pytest.mark.parametrize("repo_cls, model", [(UserRepository, User), (ChatRepository, Chat), (TicketRepository, Ticket)])
def test_repository_create_and_lookup(repo_cls, model):
    collection = FakeCollection()
    repo = repo_cls(collection=collection)
    payload = model(
        name="Test",
        email="test@example.com",
        password_hash="hash",
        subject="Example",
        content="hi",
        user_id="user-1",
    ) if repo_cls is UserRepository else model(
        user_id="user-1",
        subject="Example",
        content="hi",
    ) if repo_cls is ChatRepository else model(
        user_id="user-1",
        subject="Example",
        content="hi",
    )
    created = asyncio.run(repo.create(payload))
    assert created.id is not None
    fetched = asyncio.run(repo.get_by_id(created.id))
    assert fetched is not None
    assert fetched.id == created.id


def test_user_repository_soft_delete_and_restore():
    collection = FakeCollection()
    repo = UserRepository(collection=collection)
    user = User(name="Soft Delete", email="restore@example.com", password_hash="hash")
    created = asyncio.run(repo.create(user))
    deleted = asyncio.run(repo.soft_delete(created.id))
    assert deleted.is_deleted is True
    assert asyncio.run(repo.get_by_id(created.id)) is None
    restored = asyncio.run(repo.restore(created.id))
    assert restored.is_deleted is False
