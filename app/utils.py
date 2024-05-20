import requests
from app.crud import create_pokemon
from app.schemas import PokemonCreate
from app.database import async_session
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

async def fetch_and_store_pokemons():
    url = "https://pokeapi.co/api/v2/pokemon?limit=151"
    response = requests.get(url)
    data = response.json()

    async with async_session() as session:
        for item in data['results']:
            pokemon_data = requests.get(item['url']).json()
            pokemon = PokemonCreate(
                name=pokemon_data['name'],
                image=pokemon_data['sprites']['front_default'],
                types=[t['type']['name'] for t in pokemon_data['types']]
            )
            await create_pokemon(session, pokemon)
