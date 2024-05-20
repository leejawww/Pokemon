from fastapi import APIRouter, Depends, HTTPException
from app.core.use_cases.manage_pokemon import ManagePokemon
from app.core.repositories.pokemon_repository import PokemonRepository 
from app.models import pokemons

router = APIRouter()

@router.post("/pokemons")
async def create_pokemon(name: str, image: str, types: list, manage_pokemon: ManagePokemon = Depends()):
    created_pokemon = await manage_pokemon.create_pokemon(name=name, image=image, types=types)
    return created_pokemon
