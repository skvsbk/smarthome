"""Описание таблицы probe_location"""

from sqlalchemy import Column, Integer, String
from app.models.database import Base


class ProbeLocationDB(Base):
    __tablename__ = "probe_location"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
