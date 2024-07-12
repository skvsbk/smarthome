"""Модуль CRUD для ESP32"""

from sqlalchemy.orm import Session
from .base import create_base
from app.schemas.measurement import MeasurementCreate
from app.models.measurement import MeasurementDB
from app.models.probe_setpoint import ProbeSetpointDB


def get_setpoint(db: Session, probe_id: int):
    """Получить резалтсет для датчика"""
    res = db.query(ProbeSetpointDB).filter(ProbeSetpointDB.probe_id == probe_id).first()
    return res


def post_measurement(db: Session, value: MeasurementCreate):
    """Записать измерения датчика"""
    # TODO переделать на MQTT
    res = MeasurementDB(probe_id=value.probe_id,
                        datetime_created=value.datetime_created,
                        t1=value.t1,
                        t2=value.t2,
                        t3=value.t3,
                        l1=value.l1,
                        l2=value.l2
                        )
    create_base(db=db, value=res)
    return res
