from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import User
from src.database.repositories import UserRepository
from src.database.usecases.user import GetUser


class UserService:
    def __init__(self, session: AsyncSession):
        self.repo = UserRepository(session)

    async def get(self, user_id: int) -> Optional[User]:
        return await GetUser(self.repo)(user_id)
