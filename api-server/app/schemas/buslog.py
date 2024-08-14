"""Валидация таблицы buslog"""

from datetime import datetime
from pydantic import BaseModel


class BuslogBase(BaseModel):
    probe_id: int
    probe_location: str
    source: str
    error: str


class BuslogCreate(BuslogBase):
    datetime_created: datetime