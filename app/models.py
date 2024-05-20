from sqlalchemy import Table, Column, Integer, String, ARRAY, MetaData

metadata = MetaData()

pokemons = Table(
    'pokemons', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, index=True),
    Column('image', String),
    Column('types', ARRAY(String)),
)
