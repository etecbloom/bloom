from pydantic import BaseModel
from infra.enum import ExpLevelEnum, RoleEnum

class UserCreate(BaseModel):
    name: str
    email: str
    exp_level: ExpLevelEnum = ExpLevelEnum.NOVICE
    role: RoleEnum

class UserRead(UserCreate):
    id: int

class Config:
    orm_mode = True
