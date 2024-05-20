# Pokemon API

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/leejawww/Pokemon

3. Navigate to the project directory:
    ```bash
    cd pokemon-api

5. Install dependencies:
    ```bash
   pdm install

7. Initialize the database:
    ```bash
   pdm run alembic upgrade head

9. Run the application:
    ```bash
   pdm run python -m app.entrypoints.main

11. Access the API documentation at `http://localhost:8000/docs`.
