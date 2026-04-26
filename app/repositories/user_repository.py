from typing import Optional, List
import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from ..domain.repositories import UserRepositoryInterface
from ..domain.user import User
from ..infrastructure.models import UserEntity

logger = logging.getLogger(__name__)

class UserRepository(UserRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> Optional[User]:
        try:
            logger.debug(f"Buscando usuario por email: {email}")
            db_user = self.db.query(UserEntity).filter(UserEntity.email == email).first()
            if db_user:
                logger.debug(f"Usuario encontrado: {email} (ID: {db_user.id})")
            else:
                logger.debug(f"Usuario no encontrado: {email}")
            return User.from_orm(db_user) if db_user else None
        except SQLAlchemyError as e:
            logger.error(f"Error al buscar usuario por email {email}: {e}")
            raise

    def create(self, user: User) -> User:
        try:
            logger.debug(f"Creando usuario en BD: {user.email}")
            db_user = UserEntity(
                email=user.email,
                name=user.name,
                surname=user.surname
            )
            self.db.add(db_user)
            self.db.commit()
            self.db.refresh(db_user)
            logger.info(f"Usuario creado exitosamente: {user.email} (ID: {db_user.id})")
            return User.from_orm(db_user)
        except IntegrityError as e:
            self.db.rollback()
            logger.warning(f"Error de integridad al crear usuario {user.email}: {e}")
            raise ValueError("El email ya está registrado") from e
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"Error de base de datos al crear usuario {user.email}: {e}")
            raise
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error inesperado al crear usuario {user.email}: {e}")
            raise

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        try:
            logger.debug(f"Buscando usuario por ID: {user_id}")
            db_user = self.db.query(UserEntity).filter(UserEntity.id == user_id).first()
            if db_user:
                logger.debug(f"Usuario encontrado: ID {user_id} - {db_user.email}")
            else:
                logger.debug(f"Usuario no encontrado: ID {user_id}")
            return User.from_orm(db_user) if db_user else None
        except SQLAlchemyError as e:
            logger.error(f"Error al buscar usuario por ID {user_id}: {e}")
            raise

    def get_all_users(self) -> List[User]:
        try:
            logger.debug("Obteniendo todos los usuarios")
            db_users = self.db.query(UserEntity).all()
            logger.debug(f"Encontrados {len(db_users)} usuarios en BD")
            return [User.from_orm(db_user) for db_user in db_users]
        except SQLAlchemyError as e:
            logger.error(f"Error al obtener todos los usuarios: {e}")
            raise

    def count_users(self) -> int:
        try:
            logger.debug("Contando usuarios en BD")
            count = self.db.query(UserEntity).count()
            logger.debug(f"Conteo de usuarios: {count}")
            return count
        except SQLAlchemyError as e:
            logger.error(f"Error al contar usuarios: {e}")
            raise