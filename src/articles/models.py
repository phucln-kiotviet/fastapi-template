from ..database import Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID, TEXT
from datetime import datetime
import uuid


class Articles(Base):
    __tablename__ = "articles"

    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid.uuid4)
    title = Column(String(255), index=True)
    content = Column(TEXT)
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), onupdate=datetime.now())
    deleted = Column(DateTime())

    def __repr__(self):
        return f"{self.title}"
