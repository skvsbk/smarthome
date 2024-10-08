"""Модуль сохранения измерений"""
from core.executor import MethodParams
from core.method import register_method


@register_method(method_name="m_measurement_create")
async def sh_measurement_create(params: MethodParams):
    """Метод сохранения измерений"""
    return {"status": "ok"}

