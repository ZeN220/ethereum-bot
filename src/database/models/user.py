from sqlalchemy import Column, Integer

from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"User <id={self.id}>"
