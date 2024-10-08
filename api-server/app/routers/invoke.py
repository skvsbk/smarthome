"""Основной эндпоинт для всех запросов"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controller.invokation import invocation
from pydantic import BaseModel

from app.models.database import get_db

router = APIRouter()

class Body(BaseModel):
    method: str
    parameters: list

@router.post("/")
async def invoke(body: Body, db: Session = Depends(get_db)):

    res = await invocation(body, db)
    return res
