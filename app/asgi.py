import asyncio
from dotenv import load_dotenv
from litestar import Litestar
from litestar.di import Provide
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin

from app.database import get_db_session, init_db
from app.models import User
from app.routes import UserController

load_dotenv()

app = Litestar(
    route_handlers=[UserController],
    dependencies={"db_session": Provide(get_db_session)},
    on_startup=[init_db],
    openapi_config=OpenAPIConfig(
        title="User Management API",
        description="REST API for managing users",
        version="1.0.0",
        render_plugins=[SwaggerRenderPlugin()],
    ),
) 