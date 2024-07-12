"""Валидация таблицы probe_location"""


from pydantic import BaseModel


class ProbeLocationBase(BaseModel):
    id: int
    name: str
