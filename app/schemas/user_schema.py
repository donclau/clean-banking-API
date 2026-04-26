from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    name: str
    surname: str

class UserCreate(UserBase):
    pass  # Datos necesarios para crear

class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True) # Para que Pydantic lea modelos de SQLAlchemy