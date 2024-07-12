"""Маршруты для ESP32"""

from fastapi import APIRouter, Depends, HTTPException
from app.crud.probe import get_setpoint
from app.schemas.probe_setpoint import ProbeSetpointGet
from app.schemas.measurement import MeasurementCreate
from app.crud.probe import post_measurement

from sqlalchemy.orm import Session
from app.models.database import get_db

router = APIRouter()


@router.get("/", response_model=ProbeSetpointGet)
async def get_probe_setpoint(probe_id: int, db: Session = Depends(get_db)):
    """Получить резалтсет с уставками для датчика"""
    res = get_setpoint(db=db, probe_id=probe_id)
    if not res:
        raise HTTPException(status_code=200, detail="Probe not found")
    return res


@router.post("/")
def create_measurement(value: MeasurementCreate, db: Session = Depends(get_db)):
    """Записать измерения датчика"""
    # TODO переделать на MQTT
    post_measurement(db=db, value=value)
    return {"status": 200}
