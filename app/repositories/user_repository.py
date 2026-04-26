from sqlalchemy.orm import Session
from ..infrastructure.models import UserEntity
from ..schemas.user_schema import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str):
        return self.db.query(UserEntity).filter(UserEntity.email == email).first()

    def create(self, user_data: UserCreate):
        try:
            db_user = UserEntity(**user_data.model_dump())
            self.db.add(db_user)
            self.db.commit() # Si el servicio hace varias cosas, el commit podría ir en el Service
            self.db.refresh(db_user)
            return db_user
        except Exception as e:
            self.db.rollback()
            raise e