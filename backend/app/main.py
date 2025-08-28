from fastapi import FastAPI

from .modules.user.controller import router as user_router

app = FastAPI()

app.include_router(user_router)