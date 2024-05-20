from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.crud import get_pokemons, get_pokemon, get_pokemons_by_name_and_type, create_pokemon
from app.schemas import Pokemon, PokemonCreate
from app.database import get_db

router = APIRouter()

@router.get("/pokemons", response_model=List[Pokemon])
async def read_pokemons(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    pokemons = await get_pokemons(db, skip=skip, limit=limit)
    return pokemons

@router.get("/pokemons/filter", response_model=List[Pokemon])
async def read_pokemons_by_name_and_type(name: str = None, type_: str = None, db: AsyncSession = Depends(get_db)):
    pokemons = await get_pokemons_by_name_and_type(db, name=name, type_=type_)
    return pokemons

@router.get("/pokemon/{id}", response_model=Pokemon)
async def read_pokemon(id: int, db: AsyncSession = Depends(get_db)):
    db_pokemon = await get_pokemon(db, id)
    if db_pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return db_pokemon

@router.post("/pokemons", response_model=Pokemon)
async def create_new_pokemon(pokemon: PokemonCreate, db: AsyncSession = Depends(get_db)):
    return await create_pokemon(db, pokemon)
