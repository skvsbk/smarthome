"""Валидация таблицы probe_type"""

from pydantic import BaseModel


class ProbeTypeBase(BaseModel):
    id: int
    name: str
