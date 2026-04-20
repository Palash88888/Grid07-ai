from fastapi import APIRouter
from pydantic import BaseModel
from app.services.langgraph_flow import generate_post

generator_router = APIRouter()

class Input(BaseModel):
    bot_id: str

@generator_router.post("/")
def generate(data: Input):
    return generate_post(data.bot_id)
