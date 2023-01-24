from abc import ABC, abstractmethod
from typing import Optional

from src.database.models import User
from src.database.repositories import UserRepository


class UserUseCase(ABC):
    def __init__(self, user_repository: UserRepository):
        self.repo = user_repository

    @abstractmethod
    async def __call__(self, *args, **kwargs):
        ...


class GetUserUseCase(UserUseCase):
    async def __call__(self, user_id: int) -> Optional[User]:
        result = await self.repo.get_by_id(user_id)
        return result