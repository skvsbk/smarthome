"""Модуль CRUD для ESP32"""

from app.models.measurement import MeasurementDB
from app.models.probe_setpoint import ProbeSetpointDB
from app.schemas.measurement import MeasurementCreate
from core.utils import get_logger
from sqlalchemy.orm import Session

from .base import create_base

log = get_logger(__name__)


def setpoint_get(db: Session, probe_id: int):
    """Получить резалтсет для датчика"""
    try:
        res = db.query(ProbeSetpointDB).filter(ProbeSetpointDB.probe_id == probe_id).first()
        return res
    except Exception as e:
        log.error(str(e))
        return {"error": str(e)}


def setpiont_set(db: Session, value: MeasurementCreate):
    """Записать измерения датчика"""
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
