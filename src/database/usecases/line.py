from abc import ABC, abstractmethod

from src.database.models import Line
from src.database.repositories import LineRepository


class LineUseCase(ABC):
    def __init__(self, line_repository: LineRepository):
        self.repo = line_repository

    @abstractmethod
    async def __call__(self, *args, **kwargs):
        ...


class CreateLines(LineUseCase):
    async def __call__(
        self, seeds: list[str], user_id: int
    ) -> tuple[list[Line], int]:
        lines = []
        duplicates = 0
        for seed in seeds:
            exists = await self.repo.get(seed)
            if exists:
                duplicates += 1
                continue
            line = Line(seed=seed, user_id=user_id)
            await self.repo.create(line)
            lines.append(line)
        await self.repo.commit()
        return lines, duplicates
