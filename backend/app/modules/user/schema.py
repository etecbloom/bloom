from pydantic import BaseModel, EmailStr
from datetime import datetime
from app.shared.utils import ExperienceLevel, Role

class BaseUserSchema(BaseModel):
    email: EmailStr
    username: str
    role: Role
    exp_level: ExperienceLevel

class CreateUserSchema(BaseModel):
    username: str 
    email: EmailStr
    password:str
    exp_level: ExperienceLevel = ExperienceLevel.YOUNG
    role: Role

class ResponseUserSchema(BaseModel):
    id: int
    email: EmailStr
    username: str
    role: Role
    exp_level: ExperienceLevel
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True