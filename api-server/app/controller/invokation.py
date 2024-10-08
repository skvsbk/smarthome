from core.executor import MethodExecutor


async def invocation(method_request, db):
    try:
        executor = MethodExecutor(method_request, db)
        return await executor.execute()
    except:
        return {"status": "error"}



