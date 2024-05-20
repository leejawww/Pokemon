from pydantic import BaseModel
from typing import List

class PokemonBase(BaseModel):
    name: str
    image: str
    types: List[str]

class PokemonCreate(PokemonBase):
    pass

class Pokemon(PokemonBase):
    id: int

    class Config:
        orm_mode = True
