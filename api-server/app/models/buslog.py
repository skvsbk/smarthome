"""Описание таблицы buslog"""

from sqlalchemy import Column, Integer, String, DateTime
from app.models.database import Base


class BuslogDB(Base):
    __tablename__ = "buslog"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    probe_id = Column(Integer)
    probe_location = Column(String(100))
    source = Column(String(100))
    error = Column(String(200))
    datetime_created = Column(DateTime)
