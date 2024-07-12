"""Модуль запуска API сервера"""

from fastapi import FastAPI
import uvicorn
from app.routers import probe, application

app = FastAPI(title="SmartHome API server")

app.include_router(probe.router, prefix="/probe", tags=["room_probe"])
app.include_router(application.router, prefix="/aplication", tags=["aplication"])


# @app.on_event('shutdown')
# async def shutdown():
#     # await database.disconnect()
#     pass


if __name__ == "__main__":
    uvicorn.run("app.main:app", port=8000, host="0.0.0.0", reload=True)
