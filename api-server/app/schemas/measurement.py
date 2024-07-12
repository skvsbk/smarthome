"""Валидация таблицы measurement"""

from datetime import datetime
from pydantic import BaseModel


class MeasurementBase(BaseModel):
    probe_id: int
    t1: float | None
    t2: float | None
    t3: float | None
    l1: float | None
    l2: float | None


class MeasurementGet(MeasurementBase):
    id: int

    class Config:
        orm_mode = True


class MeasurementCreate(MeasurementBase):
    datetime_created: datetime
