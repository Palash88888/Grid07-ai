from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.router import router_router
from app.routes.generator import generator_router
from app.routes.defender import defender_router

app = FastAPI(title="Grid07 AI Cognitive System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_router, prefix="/api/router")
app.include_router(generator_router, prefix="/api/generate")
app.include_router(defender_router, prefix="/api/defend")
