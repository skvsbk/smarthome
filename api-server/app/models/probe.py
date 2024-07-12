"""Описание таблицы probe"""

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.probe_location import ProbeLocationDB
from app.models.probe_type import ProbeTypeDB


class ProbeDB(Base):
    __tablename__ = "probe"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    location_id = Column(Integer, ForeignKey("probe_location.id"), index=True)
    probe_type_id = Column(Integer, ForeignKey("probe_type.id"), index=True)

    probe_location = relationship("ProbeLocationDB")  # , backref='nfc_tag')
    probe_type = relationship("ProbeTypeDB")
