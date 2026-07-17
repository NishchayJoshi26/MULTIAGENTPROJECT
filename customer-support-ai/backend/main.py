from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes.agents import router as agents_router
from backend.api.routes.auth import router as auth_router
from backend.api.routes.chat import router as chat_router
from backend.api.routes.admin import router as admin_router
from backend.api.routes.knowledge import router as knowledge_router
from backend.api.routes.feedback import router as feedback_router
from backend.api.routes.health import router as health_router
from backend.config.logging import configure_logging
from backend.config.settings import settings
from backend.middleware.error_handler import register_exception_handlers
from backend.middleware.rate_limiter import InMemoryRateLimiter
from backend.middleware.security import SecurityHeadersMiddleware

configure_logging()

app = FastAPI(
    title=settings.app_name,
    version=settings.api_version,
    description="Backend foundation for the Multi-Agent AI Customer Support Assistant",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(InMemoryRateLimiter, limit_per_minute=settings.rate_limit_per_minute)

register_exception_handlers(app)

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(admin_router)
app.include_router(knowledge_router)
app.include_router(feedback_router)
app.include_router(agents_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.main:app", host=settings.server_host, port=settings.server_port, reload=settings.debug)
