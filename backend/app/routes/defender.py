from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag import generate_defense_reply

defender_router = APIRouter()

class Input(BaseModel):
    bot_id: str
    parent_post: str
    history: list
    reply: str

@defender_router.post("/")
def defend(data: Input):
    return {
        "response": generate_defense_reply(
            data.bot_id,
            data.parent_post,
            data.history,
            data.reply
        )
    }
