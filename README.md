# Pokemon API

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone
   https://github.com/leejawww/Pokemon

2. Navigate to the project directory:
    ```bash
    cd pokemon-api

3. Install dependencies:
    ```bash
   pdm install

4. Initialize the database:
    ```bash
   pdm run alembic upgrade head

5. Run the application:
    ```bash
   pdm run python -m app.entrypoints.main

6. Access the API documentation at
   ```bash
   `http://localhost:8000/docs`.
