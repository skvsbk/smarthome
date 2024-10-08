"""Модуль записи в БД"""

def create_base(db, value):
    """Создание или апдейт записи в БД"""
    db.add(value)
    db.commit()
    db.refresh(value)
