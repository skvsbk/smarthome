"""Модуль CRUD для ESP32"""

from sqlalchemy.orm import Session
from .base import create_base
from app.schemas.measurement import MeasurementCreate
from app.schemas.buslog import BuslogCreate
from app.models.measurement import MeasurementDB
from app.models.probe_setpoint import ProbeSetpointDB
from app.models.probe_location import ProbeLocationDB
from app.models.probe import ProbeDB
from app.models.buslog import BuslogDB


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


def post_buslog(db: Session, value: BuslogCreate):
    """Записать ошибки датчика"""
    probe_location = db.query(ProbeLocationDB.name.label("probe_location")).join(ProbeDB, ProbeDB.location_id == ProbeLocationDB.id).filter(ProbeDB.id == value.probe_id).first()

    """    
        res = db.query(nfc.NfcTagDB.id.label("nfc_id"),
                   nfc.NfcTagDB.active.label("nfc_active"),
                   plants.PlantsDB.name.label("plant_name")). \
        join(nfc.NfcTagDB, nfc.NfcTagDB.plant_id == plants.PlantsDB.id). \
        filter(plants.PlantsDB.facility_id == facility_id,
               nfc.NfcTagDB.nfc_serial == nfc_serial,
               nfc.NfcTagDB.active == True).first()
               """
    res = BuslogDB(probe_id=value.probe_id,
                   datetime_created=value.datetime_created,
                   probe_location=probe_location[0],
                   source=value.source,
                   error=value.error
                   )
    create_base(db=db, value=res)
    return res