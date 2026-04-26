from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..infrastructure.database import get_db
from ..repositories.user_repository import UserRepository
from ..services.user_service import UserService
from ..schemas.user_schema import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

# Inyectamos el Repositorio y el Servicio
def get_user_service(db: Session = Depends(get_db)):
    repository = UserRepository(db)
    return UserService(repository)

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user_in: UserCreate, service: UserService = Depends(get_user_service)):
    return service.register_user(user_in)