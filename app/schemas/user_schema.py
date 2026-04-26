from pydantic import BaseModel, EmailStr, ConfigDict, Field, field_validator
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr = Field(..., description="Email del usuario", examples=["user@example.com"])
    name: str = Field(..., min_length=1, max_length=100, description="Nombre del usuario", examples=["Juan"])
    surname: str = Field(..., min_length=1, max_length=100, description="Apellido del usuario", examples=["Pérez"])

    @field_validator('name', 'surname')
    @classmethod
    def validate_name_fields(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError('Este campo no puede estar vacío')
        if not all(c.isalpha() or c.isspace() for c in v):
            raise ValueError('Solo se permiten letras y espacios')
        return v.strip()

class UserCreate(UserBase):
    """Schema para crear un nuevo usuario"""
    pass

class UserResponse(UserBase):
    id: int = Field(..., description="ID único del usuario", examples=[1])
    created_at: datetime = Field(..., description="Fecha de creación del usuario")

    model_config = ConfigDict(from_attributes=True)

class ErrorResponse(BaseModel):
    """Schema para respuestas de error"""
    error: str = Field(..., description="Tipo de error")
    message: str = Field(..., description="Mensaje descriptivo del error")
    details: Optional[dict] = Field(None, description="Detalles adicionales del error")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Timestamp del error")

    model_config = ConfigDict(from_attributes=True)