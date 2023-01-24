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


class GetUser(UserUseCase):
    async def __call__(self, user_id: int) -> Optional[User]:
        result = await self.repo.get_by_id(user_id)
        return result


class CreateUser(UserUseCase):
    async def __call__(self, user_id: int) -> User:
        user = User(id=user_id)
        await self.repo.create(user)
        await self.repo.commit()
        return user
