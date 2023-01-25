from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Line
from src.database.repositories import LineRepository
from src.database.usecases.line import CreateLines


class LineService:
    def __init__(self, session: AsyncSession):
        self.repo = LineRepository(session)

    async def create_many(
        self, seed: list[str], user_id: int
    ) -> tuple[list[Line], int]:
        return await CreateLines(self.repo)(seeds=seed, user_id=user_id)
