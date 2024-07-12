"""Валидация таблицы probe_setpoint"""

from pydantic import BaseModel


class ProbeSetpointBase(BaseModel):
    probe_id: int
    t1: float | None
    t2: float | None
    t3: float | None
    l1: float | None
    l2: float | None


class ProbeSetpointGet(ProbeSetpointBase):

    class Config:
        orm_mode = True
