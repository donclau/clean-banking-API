import logging
from typing import List
from fastapi import HTTPException, status
from pydantic import ValidationError
from ..domain.user import User
from ..domain.repositories import UserRepositoryInterface
from ..schemas.user_schema import UserCreate

logger = logging.getLogger(__name__)

class UserService:
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def register_user(self, user_data: UserCreate) -> User:
        try:
            # Validar datos de entrada
            if not user_data.email or not user_data.email.strip():
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El email es obligatorio"
                )

            if not user_data.name or not user_data.name.strip():
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El nombre es obligatorio"
                )

            if not user_data.surname or not user_data.surname.strip():
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El apellido es obligatorio"
                )

            # Verificar si el email ya existe
            existing_user = self.repository.get_by_email(user_data.email.strip().lower())
            if existing_user:
                logger.warning(f"Intento de registro con email duplicado: {user_data.email}")
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Ya existe un usuario con este email"
                )

            # Crear el usuario
            user = User(
                email=user_data.email.strip().lower(),
                name=user_data.name.strip(),
                surname=user_data.surname.strip()
            )

            created_user = self.repository.create(user)
            logger.info(f"Usuario registrado exitosamente: {user_data.email} (ID: {created_user.id})")
            return created_user

        except HTTPException:
            # Re-lanzar excepciones HTTP ya manejadas
            raise
        except ValidationError as e:
            # Error de validación de Pydantic
            logger.warning(f"Error de validación al registrar usuario: {e}")
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Datos inválidos: {str(e)}"
            )
        except ValueError as e:
            # Error específico de negocio (como email duplicado desde repo)
            logger.warning(f"Error de negocio al registrar usuario: {e}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
        except Exception as e:
            logger.error(f"Error inesperado al registrar usuario {getattr(user_data, 'email', 'unknown')}: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error interno del servidor. Intente nuevamente más tarde."
            )

    def get_user_by_id(self, user_id: int) -> User:
        try:
            # Validar que el ID sea un entero positivo
            if not isinstance(user_id, int) or user_id <= 0:
                logger.warning(f"ID de usuario inválido recibido: {user_id} (tipo: {type(user_id)})")
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El ID del usuario debe ser un número entero positivo"
                )

            # Validar rango razonable de IDs
            if user_id > 999999:
                logger.warning(f"ID de usuario potencialmente inválido: {user_id}")
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="ID de usuario inválido"
                )

            user = self.repository.get_user_by_id(user_id)
            if not user:
                logger.warning(f"Usuario no encontrado: {user_id}")
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"No se encontró un usuario con ID {user_id}"
                )

            logger.debug(f"Usuario {user_id} encontrado: {user.email}")
            return user

        except HTTPException:
            # Re-lanzar excepciones HTTP ya manejadas
            raise
        except Exception as e:
            logger.error(f"Error al obtener usuario {user_id}: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error interno del servidor al consultar el usuario"
            )

    def get_all_users(self) -> List[User]:
        try:
            users = self.repository.get_all_users()
            user_count = len(users)
            logger.info(f"Consulta exitosa: {user_count} usuarios obtenidos")

            # Advertir si hay muchos usuarios (posible problema de performance)
            if user_count > 1000:
                logger.warning(f"Consulta devolvió {user_count} usuarios. Considere implementar paginación.")

            return users

        except Exception as e:
            logger.error(f"Error al obtener todos los usuarios: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error interno del servidor al obtener la lista de usuarios"
            )

    def get_user_count(self) -> int:
        """
        Obtiene el número total de usuarios registrados.

        Returns:
            int: Número total de usuarios

        Raises:
            HTTPException: Si ocurre un error interno del servidor (500)
        """
        try:
            logger.info("Contando usuarios registrados")
            count = self.repository.count_users()
            logger.info(f"Conteo exitoso: {count} usuarios registrados")
            return count
        except Exception as e:
            logger.error(f"Error al contar usuarios: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error interno del servidor al contar usuarios"
            )