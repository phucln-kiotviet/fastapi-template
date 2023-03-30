from ..database import Base
from sqlalchemy import Column, String, DateTime
from datetime import datetime


class Articles(Base):
    __tablename__ = "articles"
    title = Column(String(255), unique=True, index=True)
    content = Column(String(255))
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), onupdate=datetime.now())

    def __repr__(self):
        return f"{self.title}"
