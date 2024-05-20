import httpx
from app.core.repositories.pokemon_repository import PokemonRepository

async def fetch_pokemon_data(pokemon_repo: PokemonRepository):
    url = pokemon_repo.pokeapi_url
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        pokemons = response.json()["results"]

        for pokemon in pokemons:
            pokemon_detail = await client.get(pokemon["url"])
            pokemon_detail.raise_for_status()
            data = pokemon_detail.json()

            await pokemon_repo.create_pokemon(
                id=data["id"],
                name=data["name"],
                image=data["sprites"]["front_default"],
                types=[t["type"]["name"] for t in data["types"]]
            )
