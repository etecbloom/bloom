from fastapi import FastAPI
from features.user.router import router as user_router
from infra.database import Base, engine

app = FastAPI()

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app.include_router(user_router, prefix="/users", tags=["Users"])
