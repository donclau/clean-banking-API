from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class AccountEntity(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    account_number = Column(String(22), unique=True, nullable=False)
    alias = Column(String(50), unique=True, nullable=False)
    balance = Column(DECIMAL(12, 2), default=0.00)

    # Relación: La cuenta pertenece a un usuario
    owner = relationship("UserEntity", back_populates="accounts")