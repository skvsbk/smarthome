"""Модуль работы с методом"""

from collections import OrderedDict

from core.method import find_registered_method


class MethodExecutor:
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

    def __init__(self, index: int, name: str, value):
        self.index = index
        self.name = name
        self.value = value


    def __str__(self):
        return "%s(name=%s, value=%s)" % (self.__class__.__qualname__, len(self.name), len(self.value))

    def __repr__(self):
        return "<%s.%s: name=%s, value=%s>" % (
            self.__class__.__module__, self.__class__.__qualname__, len(self.name), len(self.value))


class MethodParams:
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
        else:
            return default
