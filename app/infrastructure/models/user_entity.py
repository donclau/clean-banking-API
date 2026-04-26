from sqlalchemy import Column, Integer, String, TIMESTAMP, Index, func
from sqlalchemy.orm import relationship
from ..database import Base

class UserEntity(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, default=func.current_timestamp())

    # Índices
    __table_args__ = (Index('idx_users_email', 'email'),)

    # Relación: Un usuario tiene muchas cuentas
    accounts = relationship("AccountEntity", back_populates="owner", cascade="all, delete-orphan")