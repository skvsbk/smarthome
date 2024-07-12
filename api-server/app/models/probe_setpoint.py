"""Описание таблицы probe_setpoint"""

from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.probe import ProbeDB


class ProbeSetpointDB(Base):
    __tablename__ = "probe_setpoint"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    probe_id = Column(Integer, ForeignKey("probe.id"), index=True)
    t1 = Column(Float)
    t2 = Column(Float)
    t3 = Column(Float)
    l1 = Column(Float)
    l2 = Column(Float)

    probe = relationship("ProbeDB")  # , backref='nfc_tag')
