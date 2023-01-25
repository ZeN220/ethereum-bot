from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    lines = relationship("Line", lazy="selectin")

    def __repr__(self):
        return f"User <id={self.id}>"
