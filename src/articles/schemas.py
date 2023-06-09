from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class ArticlesBase(BaseModel):
    title: str
    content: str | None


class ArticlesCreate(ArticlesBase):
    pass


class Articles(ArticlesBase):
    id: UUID | None
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        orm_mode = True  # Make Pydantic read the data even if it is not a dict


class ArticlesUpdate(BaseModel):
    title: str | None
    content: str | None

    class Config:
        orm_mode = True
