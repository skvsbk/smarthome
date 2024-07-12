"""Маршруты для приложения"""

from fastapi import APIRouter, Depends, HTTPException
from app.crud.application import get_setpoint, get_setpoints
from app.schemas.probe_setpoint import ProbeSetpointGet


from sqlalchemy.orm import Session
from app.models.database import get_db

router = APIRouter()


@router.get("/setpoint", response_model=ProbeSetpointGet)
async def get_probe_setpoint(probe_id: int, db: Session = Depends(get_db)):
    """Получить резалтсет с уставками для датчика"""
    res = get_setpoint(db=db, probe_id=probe_id)
    if not res:
        raise HTTPException(status_code=200, detail="Probe not found")
    return res


@router.get("/setpoints", response_model=list[ProbeSetpointGet])
async def get_probe_setpoints(db: Session = Depends(get_db)):
    """Получить резалтсет с уставками для датчика"""
    res = get_setpoints(db=db)
    if not res:
        raise HTTPException(status_code=200, detail="Probes not found")
    return res
