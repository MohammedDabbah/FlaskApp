# Flask OpenAI App

This is a simple Flask application that uses the OpenAI API to answer questions. The app stores both questions and answers in a PostgreSQL database and is fully containerized using Docker and Docker Compose.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask-openai-app.git
   cd flask-openai-app
   ```

2. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

3. Apply the database migrations:
   ```bash
   docker-compose exec web flask db upgrade
   ```

4. The Flask app will be running at `http://localhost:5001`.

## Running the Tests

1. Run the tests using pytest:
   ```bash
   docker-compose exec web pytest
   ```

## API Usage

- **Endpoint**: `/ask`
- **Method**: POST
- **Payload**:
  ```json
  {
    "question": "What is the capital of France?"
  }
  ```

## Technologies Used

- Flask
- PostgreSQL
- Docker & Docker Compose
- Alembic (for migrations)
- Pytest (for testing)

## Warnning the password and the key are used just for example the key will no longer be active . 
