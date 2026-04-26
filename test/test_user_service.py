import pytest
from fastapi import HTTPException
from typing import List

from app.schemas.user_schema import UserCreate
from app.services.user_service import UserService
from app.domain.user import User


class FakeUserRepository:
    def __init__(self, existing_user=None):
        self.existing_user = existing_user
        self.created_user = None
        self.create_called = False
        self.users = []  # For get_all_users

    def get_by_email(self, email: str):
        return self.existing_user

    def create(self, user_data: UserCreate):
        self.create_called = True
        self.created_user = User(
            id=1,
            email=user_data.email,
            name=user_data.name,
            surname=user_data.surname
        )
        self.users.append(self.created_user)
        return self.created_user

    def get_user_by_id(self, user_id: int):
        return next((user for user in self.users if user.id == user_id), None)

    def get_all_users(self) -> List[User]:
        return self.users


def test_register_user_success():
    fake_repo = FakeUserRepository(existing_user=None)
    service = UserService(repository=fake_repo)

    user_in = UserCreate(email="test@example.com", name="Test", surname="User")
    result = service.register_user(user_in)

    assert fake_repo.create_called is True
    assert result.email == "test@example.com"
    assert result.name == "Test"
    assert result.surname == "User"
    assert result.id == 1


def test_register_user_duplicate_email_raises_http_exception():
    fake_repo = FakeUserRepository(existing_user=User(id=1, email="test@example.com", name="Existing", surname="User"))
    service = UserService(repository=fake_repo)

    user_in = UserCreate(email="test@example.com", name="Test", surname="User")

    with pytest.raises(HTTPException) as exc_info:
        service.register_user(user_in)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Email ya registrado"
    assert fake_repo.create_called is False
