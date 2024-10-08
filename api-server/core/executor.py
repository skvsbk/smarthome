"""Модуль работы с методом"""

from collections import OrderedDict

from core.method import find_registered_method


class MethodExecutor:
    """Класс выполнения метода, пришедшего в api"""
    def __init__(self, invoke_request, db):
        self.invoke_request = invoke_request
        self.db = db

    async def execute(self):
        method_name = self.invoke_request.method

        func = find_registered_method(method_name)

        if not func:
            raise ValueError(f"Method registration not found: {method_name}")
        method_params = MethodParams(db=self.db)
        if self.invoke_request.parameters:
            await method_params.add_params(self.invoke_request.parameters)

        res = await func(method_params)
        return res


class MethodParam:
    """Класс описания полученных параметров для вызова методов"""
    def __init__(self, index: int, name: str, value):
        self.index = index
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.__class__.__qualname__}(name={len(self.name)}, value={len(self.value)})"

    def __repr__(self):
        return (f"<{self.__class__.__module__}.{self.__class__.__qualname__}: "
                f"name={len(self.name)}, value={len(self.value)}>")


class MethodParams:
    """Класс описания полученных параметра для вызова методов"""
    def __init__(self, db):
        self.params: dict = OrderedDict()
        self.db = db

    async def add_params(self, invoke_parameters: list):
        try:
            for index, par in enumerate(invoke_parameters):
                name = par['name']
                apitype = par['type']
                value = par.get(apitype, None)
                method_param = MethodParam(index=index, name=name, value=value)
                await self.add(method_param)
        except Exception as e:
            print(str(e))

    async def add(self, param: MethodParam):
        self.params[param.name] = param

    def __getitem__(self, name):
        return self.params[name].value

    def get(self, name: str, default=None):
        if name in self.params:
            return self.params[name].value
        return default
