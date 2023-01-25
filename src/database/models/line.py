from sqlalchemy import Column, ForeignKey, Integer, String

from .base import Base


class Line(Base):
    __tablename__ = "lines"

    id = Column(Integer, primary_key=True)
    seed = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Line <seed={self.seed}, user_id={self.user_id}>"
