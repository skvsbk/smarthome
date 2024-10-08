"""Модуль записи в БД"""

def create_base(db, value):
    db.add(value)
    db.commit()
    db.refresh(value)
