from fastapi import Request
from backend.config.settings import settings


def get_request_id(request: Request) -> str:
    return request.headers.get("x-request-id", "local")


def get_api_version() -> str:
    return settings.api_version
