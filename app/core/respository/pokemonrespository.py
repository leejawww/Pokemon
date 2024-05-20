from app.models import pokemons

class PokemonRepository:
    def __init__(self, db):
        self.db = db

    async def create_pokemon(self, name: str, image: str, types: list):
        async with self.db.begin():
            await self.db.execute(pokemons.insert().values(
                name=name,
                image=image,
                types=types
            ))
