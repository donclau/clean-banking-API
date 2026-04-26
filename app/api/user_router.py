import logging
from fastapi import APIRouter, Depends, Request, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
from pydantic import ValidationError
from ..infrastructure.database import get_db
from ..repositories.user_repository import UserRepository
from ..services.user_service import UserService
from ..schemas.user_schema import UserCreate, UserResponse, ErrorResponse

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/users", tags=["Users"])

# Inyectamos el Repositorio y el Servicio
def get_user_service(db: Session = Depends(get_db)):
    repository = UserRepository(db)
    return UserService(repository)

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo usuario",
    description="Registra un nuevo usuario en el sistema. El email debe ser único.",
    responses={
        201: {"description": "Usuario creado exitosamente", "model": UserResponse},
        400: {"description": "Datos inválidos o faltantes", "model": ErrorResponse},
        409: {"description": "Email ya registrado", "model": ErrorResponse},
        422: {"description": "Error de validación de datos", "model": ErrorResponse},
        500: {"description": "Error interno del servidor", "model": ErrorResponse}
    }
)
def create_user(request: Request, user_in: UserCreate, service: UserService = Depends(get_user_service)):
    client_ip = request.client.host if request.client else "unknown"
    logger.info(f"POST /users - Creando usuario: {user_in.email} desde IP: {client_ip}")

    try:
        result = service.register_user(user_in)
        logger.info(f"Usuario creado exitosamente: {user_in.email} (ID: {result.id})")
        return result

    except HTTPException as e:
        # Re-lanzar excepciones HTTP ya manejadas por el servicio
        logger.warning(f"Error HTTP al crear usuario {user_in.email}: {e.detail}")
        raise
    except ValidationError as e:
        logger.warning(f"Error de validación Pydantic al crear usuario: {e}")
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Datos inválidos: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error inesperado al crear usuario {user_in.email}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor"
        )

@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="Obtener usuario por ID",
    description="Consulta un usuario específico por su ID único.",
    responses={
        200: {"description": "Usuario encontrado", "model": UserResponse},
        400: {"description": "ID inválido", "model": ErrorResponse},
        404: {"description": "Usuario no encontrado", "model": ErrorResponse},
        500: {"description": "Error interno del servidor", "model": ErrorResponse}
    }
)
def get_user_by_id(request: Request, user_id: int, service: UserService = Depends(get_user_service)):
    client_ip = request.client.host if request.client else "unknown"
    logger.info(f"GET /users/{user_id} - Consultando usuario desde IP: {client_ip}")

    try:
        result = service.get_user_by_id(user_id)
        logger.info(f"Usuario {user_id} consultado exitosamente: {result.email}")
        return result

    except HTTPException as e:
        # Re-lanzar excepciones HTTP ya manejadas por el servicio
        logger.warning(f"Error HTTP al consultar usuario {user_id}: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"Error inesperado al consultar usuario {user_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor"
        )

@router.get(
    "/",
    response_model=List[UserResponse],
    summary="Listar todos los usuarios",
    description="Obtiene una lista de todos los usuarios registrados en el sistema.",
    responses={
        200: {"description": "Lista de usuarios obtenida exitosamente", "model": List[UserResponse]},
        500: {"description": "Error interno del servidor", "model": ErrorResponse}
    }
)
def get_all_users(request: Request, service: UserService = Depends(get_user_service)):
    client_ip = request.client.host if request.client else "unknown"
    logger.info(f"GET /users - Listando todos los usuarios desde IP: {client_ip}")

    try:
        result = service.get_all_users()
        logger.info(f"Listado de usuarios exitoso: {len(result)} usuarios retornados")
        return result

    except HTTPException as e:
        # Re-lanzar excepciones HTTP ya manejadas por el servicio
        logger.warning(f"Error HTTP al listar usuarios: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"Error inesperado al listar usuarios: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor"
        )

@router.get(
    "/count",
    summary="Contar usuarios",
    description="Obtiene el número total de usuarios registrados en el sistema.",
    responses={
        200: {"description": "Conteo exitoso", "model": dict},
        500: {"description": "Error interno del servidor", "model": ErrorResponse}
    }
)
def get_user_count(request: Request, service: UserService = Depends(get_user_service)):
    client_ip = request.client.host if request.client else "unknown"
    logger.info(f"GET /users/count - Contando usuarios desde IP: {client_ip}")

    try:
        count = service.get_user_count()
        logger.info(f"Conteo de usuarios exitoso: {count} usuarios")
        return {"count": count, "message": f"Total de usuarios registrados: {count}"}

    except HTTPException as e:
        # Re-lanzar excepciones HTTP ya manejadas por el servicio
        logger.warning(f"Error HTTP al contar usuarios: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"Error inesperado al contar usuarios: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor"
        )