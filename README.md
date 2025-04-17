# User Management API

A REST API for managing users built with LiteStar and PostgreSQL.

## Features

- CRUD operations for users
- PostgreSQL database
- OpenAPI (Swagger) documentation
- Docker support

## Prerequisites

- Python 3.12
- Poetry 1.8.3
- Docker and Docker Compose

## Setup

1. Clone the repository:
```bash
git clone [your-repository-url]
cd user-management-api
```

2. Install dependencies:
```bash
poetry install
```

3. Start the PostgreSQL database:
```bash
docker-compose up -d
```

4. Run the application:
```bash
poetry run litestar run app.asgi:app --host 127.0.0.1 --port 8000
```

## API Documentation

Once the application is running, you can access the Swagger documentation at:
```
http://127.0.0.1:8000/schema/swagger
```

## API Endpoints

- `GET /users` - Get all users
- `GET /users/{user_id}` - Get a specific user
- `POST /users` - Create a new user
- `PUT /users/{user_id}` - Update a user
- `DELETE /users/{user_id}` - Delete a user

## Environment Variables

Create a `.env` file with the following variables:
```
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5433/user_management
``` 