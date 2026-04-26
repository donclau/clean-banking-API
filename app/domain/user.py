from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class User:
    id: Optional[int] = None
    email: str = ""
    name: str = ""
    surname: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)

    @classmethod
    def from_orm(cls, orm_obj) -> "User":
        return cls(
            id=getattr(orm_obj, "id", None),
            email=getattr(orm_obj, "email", ""),
            name=getattr(orm_obj, "name", ""),
            surname=getattr(orm_obj, "surname", ""),
            created_at=getattr(orm_obj, "created_at", datetime.utcnow()),
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "surname": self.surname,
            "created_at": self.created_at,
        }
