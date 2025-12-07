from fastapi import APIRouter
from src.blog.schemas import PostCreate

post_router = APIRouter()

@post_router.post("/post")
def create_post(post: PostCreate) -> dict:
    return {"message": True}
