"""Описание таблицы probe_type"""

from sqlalchemy import Column, Integer, String
from app.models.database import Base


class ProbeTypeDB(Base):
    __tablename__ = "probe_type"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
