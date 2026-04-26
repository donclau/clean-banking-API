from fastapi import HTTPException, status
from ..domain.user import User
from ..domain.repositories import UserRepositoryInterface
from ..schemas.user_schema import UserCreate

class UserService:
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def register_user(self, user_data: UserCreate) -> User:
        existing_user = self.repository.get_by_email(user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email ya registrado"
            )

        user = User(
            email=user_data.email,
            name=user_data.name,
            surname=user_data.surname
        )

        return self.repository.create(user)