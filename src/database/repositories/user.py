from typing import Optional

from sqlalchemy import select

from src.database.models import User

from .base import BaseRepository


class UserRepository(BaseRepository):
    async def get_by_id(self, user_id: int) -> Optional[User]:
        statement = select(User).where(User.id == user_id)
        result = await self.session.execute(statement)
        return result.scalar()

    async def create(self, user: User) -> User:
        self.session.add(user)
        await self.session.flush()
        return user
