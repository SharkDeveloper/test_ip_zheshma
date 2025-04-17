# API управления пользователями

REST API для управления пользователями, построенное с использованием Litestar и PostgreSQL.

## Технологии

- Python 3.12
- Litestar (веб-фреймворк)
- SQLAlchemy (ORM)
- PostgreSQL (база данных)
- Poetry (управление зависимостями)
- Docker & Docker Compose (контейнеризация)

## Требования

- Docker
- Docker Compose
- Python 3.12 или выше
- Poetry

## Установка и запуск

### Локальный запуск

1. Клонируйте репозиторий:
```bash
git clone <url-репозитория>
cd <имя-директории>
```

2. Установите зависимости с помощью Poetry:
```bash
poetry install
```

3. Создайте файл `.env` в корневой директории:
```env
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5433/user_management
```

4. Запустите PostgreSQL через Docker Compose:
```bash
docker-compose up -d postgres
```

5. Запустите приложение:
```bash
poetry run uvicorn app.asgi:app --reload
```

### Запуск через Docker

1. Соберите и запустите все контейнеры:
```bash
docker-compose up --build
```

Приложение будет доступно по адресу: http://localhost:8000

## API Endpoints

### Пользователи

- `GET /users` - Получить список всех пользователей
- `GET /users/{id}` - Получить информацию о конкретном пользователе
- `POST /users` - Создать нового пользователя
- `PUT /users/{id}` - Обновить информацию о пользователе
- `DELETE /users/{id}` - Удалить пользователя

## Структура проекта

```
.
├── app/
│   ├── __init__.py
│   ├── asgi.py          # Точка входа приложения
│   ├── database.py      # Конфигурация базы данных
│   ├── models.py        # Модели данных
│   └── routes.py        # Маршруты API
├── docker-compose.yml   # Конфигурация Docker Compose
├── Dockerfile          # Конфигурация Docker
├── poetry.lock         # Фиксация версий зависимостей
├── pyproject.toml      # Конфигурация проекта и зависимости
└── README.md           # Документация
```

## Разработка

### Добавление новых зависимостей

```bash
poetry add <имя-пакета>
```

### Обновление зависимостей

```bash
poetry update
```

### Запуск тестов

```bash
poetry run pytest
```

## Лицензия

MIT 