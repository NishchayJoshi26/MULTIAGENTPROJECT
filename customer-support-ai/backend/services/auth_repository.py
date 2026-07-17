from typing import Optional

from backend.models.user import User


class AuthRepository:
    def __init__(self) -> None:
        self._users: dict[str, User] = {}

    def get_by_email(self, email: str) -> Optional[User]:
        return self._users.get(email.lower())

    def save(self, user: User) -> None:
        self._users[str(user.email).lower()] = user

    def list(self) -> list[User]:
        return list(self._users.values())
