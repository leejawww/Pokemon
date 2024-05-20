# Pokemon API

## Setup Instructions

1. Clone the repository:
    git clone https://github.com/leejawww/Pokemon

2. Navigate to the project directory:
    cd pokemon-api

3. Install dependencies:
    pdm install

4. Initialize the database:
    pdm run alembic upgrade head

5. Run the application:
    pdm run python -m app.entrypoints.main

6. Access the API documentation at `http://localhost:8000/docs`.
