"""Основной эндпоинт для всех запросов"""

from fastapi import APIRouter
from app.controller.invokation import invokation

router = APIRouter()


@router.post("/")
async def invoke(body):
    res = invokation(body)
    return res

