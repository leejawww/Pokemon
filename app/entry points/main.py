from app.entrypoints.rest.pokemon_router import router
from fastapi import FastAPI

app = FastAPI()

app.include_router(router, prefix="/api/v1")
