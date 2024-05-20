# Pokemon API

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/leejawww/Pokemon
    cd pokemon_api
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the root directory and add your database URL.
    ```plaintext
    DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
    ```

5. Run Alembic migrations to set up the database schema:
    ```bash
    alembic upgrade head
    ```

6. Load data from PokeAPI:
    ```bash
    python -m app.utils
    ```

7. Start the FastAPI server:
    ```bash
    uvicorn app.main:app --reload
    ```

8. Access the API documentation at `http://localhost:8000/docs`.

## API Endpoints

- `GET /api/v1/pokemons`: Get a list of all pokemons.
- `GET /api/v1/pokemons/filter`: Get a filtered list of pokemons by name or type.
- `GET /api/v1/pokemon/{id}`: Get details of a specific pokemon by ID.
- `POST /api/v1/pokemons`: Add a new pokemon.
