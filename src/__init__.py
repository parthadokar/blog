from fastapi import FastAPI
from src.blog.routes import post_router

app = FastAPI(title="Blog")

app.include_router(post_router)