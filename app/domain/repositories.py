from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, List
from .user import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def create(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def get_all_users(self) -> List[User]:
        raise NotImplementedError
