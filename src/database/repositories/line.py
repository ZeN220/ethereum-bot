from sqlalchemy import select

from src.database.models import Line

from .base import BaseRepository


class LineRepository(BaseRepository):
    async def get(self, seed: str) -> Line:
        statement = select(Line).where(Line.seed == seed)
        result = await self.session.execute(statement)
        return result.scalar()

    async def create(self, line: Line) -> Line:
        self.session.add(line)
        await self.session.flush()
        return line
