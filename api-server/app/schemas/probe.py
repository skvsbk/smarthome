"""Валидация таблицы probe"""

from pydantic import BaseModel


class ProbeBase(BaseModel):
    id: int
    location_id: int
    probe_type_id: int
