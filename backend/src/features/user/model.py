from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from infra.database import Base
from infra.enum import ExpLevelEnum, RoleEnum

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    exp_level = Column(Enum(ExpLevelEnum), default=ExpLevelEnum.NOVICE)
    role = Column(Enum(RoleEnum), nullable=False)   

    posts=relationship("Post", back_populates="owner")