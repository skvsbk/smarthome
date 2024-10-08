"""Модуль выполнения метода из запроса"""
from core.executor import MethodExecutor

from core.utils import get_logger

log = get_logger(__name__)


async def invocation(method_request, db):
    """Выполнение метода из запроса"""
    try:
        executor = MethodExecutor(method_request, db)
        return await executor.execute()
    except ValueError as e:
        log.error(str(e))
        return {"error": str(e)}
