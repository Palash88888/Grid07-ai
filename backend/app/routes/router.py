from fastapi import APIRouter
from pydantic import BaseModel
from app.services.vector_store import route_post_to_bots

router_router = APIRouter()

class PostInput(BaseModel):
    content: str

@router_router.post("/")
def route(post: PostInput):
    return {"matches": route_post_to_bots(post.content)}
