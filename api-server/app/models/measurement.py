"""Описание таблицы measurement"""

from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.probe import ProbeDB


class MeasurementDB(Base):
    __tablename__ = "measurement"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    probe_id = Column(Integer, ForeignKey("probe.id"), index=True)
    datetime_created = Column(DateTime)
    t1 = Column(Float)
    t2 = Column(Float)
    t3 = Column(Float)
    l1 = Column(Float)
    l2 = Column(Float)

    probe = relationship("ProbeDB")  # , backref='nfc_tag')
