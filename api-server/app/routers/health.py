"""Эндпоинт проверки доступности сервера"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def health():
    return {
        "status": "OK",
        "code": 200
    }
