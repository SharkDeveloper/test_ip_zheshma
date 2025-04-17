FROM python:3.12-slim

WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy application code first
COPY . .

# Configure poetry to not create virtual environment
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --only main

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "uvicorn", "app.asgi:app", "--host", "0.0.0.0", "--port", "8000"] 