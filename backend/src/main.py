from fastapi import FastAPI
from features.user.router import router as user_router
from features.posts.router import router as post_router
from infra.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(post_router, prefix="/posts", tags=["Posts"])