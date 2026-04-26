import pytest
from fastapi import HTTPException

from app.schemas.user_schema import UserCreate
from app.services.user_service import UserService


class FakeUserRepository:
    def __init__(self, existing_user=None):
        self.existing_user = existing_user
        self.created_user = None
        self.create_called = False

    def get_by_email(self, email: str):
        return self.existing_user

    def create(self, user_data: UserCreate):
        self.create_called = True
        self.created_user = {
            "id": 1,
            "email": user_data.email,
            "name": user_data.name,
            "surname": user_data.surname,
            "created_at": "2026-04-26T10:00:00"
        }
        return self.created_user


def test_register_user_success():
    fake_repo = FakeUserRepository(existing_user=None)
    service = UserService(repository=fake_repo)

    user_in = UserCreate(email="test@example.com", name="Test", surname="User")
    result = service.register_user(user_in)

    assert fake_repo.create_called is True
    assert result["email"] == "test@example.com"
    assert result["name"] == "Test"
    assert result["surname"] == "User"
    assert result["id"] == 1


def test_register_user_duplicate_email_raises_http_exception():
    fake_repo = FakeUserRepository(existing_user={"email": "test@example.com"})
    service = UserService(repository=fake_repo)

    user_in = UserCreate(email="test@example.com", name="Test", surname="User")

    with pytest.raises(HTTPException) as exc_info:
        service.register_user(user_in)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Email ya registrado"
    assert fake_repo.create_called is False
