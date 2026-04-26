from typing import Optional, List

from sqlalchemy.orm import Session

from ..domain.repositories import UserRepositoryInterface
from ..domain.user import User
from ..infrastructure.models import UserEntity

class UserRepository(UserRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> Optional[User]:
        db_user = self.db.query(UserEntity).filter(UserEntity.email == email).first()
        return User.from_orm(db_user) if db_user else None

    def create(self, user: User) -> User:
        try:
            db_user = UserEntity(
                email=user.email,
                name=user.name,
                surname=user.surname
            )
            self.db.add(db_user)
            self.db.commit()  # Si el servicio hace varias cosas, el commit podría ir en el Service
            self.db.refresh(db_user)
            return User.from_orm(db_user)
        except Exception as e:
            self.db.rollback()
            raise e

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        db_user = self.db.query(UserEntity).filter(UserEntity.id == user_id).first()
        return User.from_orm(db_user) if db_user else None

    def get_all_users(self) -> List[User]:
        db_users = self.db.query(UserEntity).all()
        return [User.from_orm(db_user) for db_user in db_users]