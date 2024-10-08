"""Модуль CRUD для мобильного приложения"""

from app.models.probe_setpoint import ProbeSetpointDB
from sqlalchemy.orm import Session


def get_setpoint(db: Session, probe_id: int):
    """Получить уставки для датчика"""
    res = db.query(ProbeSetpointDB).filter(ProbeSetpointDB.probe_id == probe_id).first()
    return res


def get_setpoints(db: Session):
    """Получить уставки для всех датчиков"""
    res = db.query(ProbeSetpointDB).offset(0).limit(100).all()
    return res


def create_setpoint(db: Session):
    pass


def create_location(db: Session):
    pass


def create_probe_type(db: Session):
    pass


def create_probe(db: Session):
    pass
