from collections import defaultdict
from time import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


class InMemoryRateLimiter(BaseHTTPMiddleware):
    def __init__(self, app, limit_per_minute: int = 60):
        super().__init__(app)
        self.limit_per_minute = limit_per_minute
        self.requests = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host if request.client else "unknown"
        now = time()
        self.requests[client_ip] = [timestamp for timestamp in self.requests[client_ip] if now - timestamp < 60]
        if len(self.requests[client_ip]) >= self.limit_per_minute:
            return Response(status_code=429, content='{"detail":"Rate limit exceeded"}', media_type='application/json')
        self.requests[client_ip].append(now)
        return await call_next(request)
