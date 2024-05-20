from app.core.repositories.pokemon_repository import PokemonRepository

class ManagePokemon:
    def __init__(self, pokemon_repo: PokemonRepository):
        self.pokemon_repo = pokemon_repo

    async def create_pokemon(self, name: str, image: str, types: list):
        return await self.pokemon_repo.create_pokemon(name=name, image=image, types=types)
