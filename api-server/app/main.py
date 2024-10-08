"""Модуль запуска API сервера"""

from fastapi import FastAPI
import uvicorn
from app.routers import health, invoke
from core.method import make_methods_registry

app = FastAPI(title="SmartHome API server")

app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(invoke.router, prefix="/invoke", tags=["invoke"])
make_methods_registry("methods")

if __name__ == "__main__":
    uvicorn.run("app.main:app", port=8000, host="0.0.0.0", reload=True)
