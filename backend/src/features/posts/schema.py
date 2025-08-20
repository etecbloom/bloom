from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime | None
    user_id: int

    class Config:
        orm_mode = True
