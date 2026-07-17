from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config.settings import settings
from backend.config.logging import configure_logging

configure_logging()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Initial scaffold for the Multi-Agent AI Customer Support Assistant",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": settings.app_name}
