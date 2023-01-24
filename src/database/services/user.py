from sqlalchemy.ext.asyncio import AsyncSession

from src.database.repositories import UserRepository
from src.database.usecases.user import GetUserUseCase


class UserService:
    def __init__(self, session: AsyncSession):
        self.repo = UserRepository(session)

    async def get(self, user_id: int) -> GetUserUseCase:
        return await GetUserUseCase(self.repo)(user_id)
