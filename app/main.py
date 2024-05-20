from fastapi import FastAPI
from app.routers import pokemon
import uvicorn

app = FastAPI()

app.include_router(pokemon.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
