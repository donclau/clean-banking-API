from fastapi import HTTPException, status
from ..repositories.user_repository import UserRepository
from ..schemas.user_schema import UserCreate

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register_user(self, user_data: UserCreate):
        # Lógica de negocio
        existing_user = self.repository.get_by_email(user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Email ya registrado"
            )
        return self.repository.create(user_data)