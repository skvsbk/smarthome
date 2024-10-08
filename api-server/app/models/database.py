"""Модуль подключения к БД"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv, find_dotenv
from config.settings import DB_ADDR, DB_NAME, DB_PASS, DB_PORT, DATABASE

# config = Config('.env_db')

DATABASE_URL = f"mysql+pymysql://{DB_NAME}:{DB_PASS}@{DB_ADDR}:{DB_PORT}/{DATABASE}?charset=utf8mb4"
# load_dotenv(find_dotenv('./.env_db'))
# DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
