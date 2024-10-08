"""Модуль регистрации методов"""

import importlib
import os
import sys

from core.utils import get_logger

log = get_logger(__name__)

_registered_methods = {}


def register_method(method_name: str):
    """Декоратор регистрации методов"""
    def wrap(func):
        # global _registered_methods
        if method_name in _registered_methods:
            if _registered_methods[method_name] == func:
                return func
            log.error("### method  %s => %s.%s() already register to %s.%s()", method_name, func.__module__,
                      func.__name__, _registered_methods[method_name].__module__,
                      _registered_methods[method_name].__name__)

            sys.exit(1)
        log.info("### register method  %s => %s.%s()", method_name, func.__module__, func.__name__)
        _registered_methods[method_name] = func
        return func
    return wrap


def make_methods_registry(folder_name: str):
    """Зарегистрировать методы из директории folder_name с декоратором @register_method"""
    method_root = importlib.import_module(folder_name)
    root, _ = os.path.split(method_root.__file__)
    _import_package(folder_name, root)


def _import_package(base_package, package_dir):
    """Рекурсивное добавление методов и модулей"""
    for f in os.listdir(package_dir):
        ff = os.path.join(package_dir, f)
        if os.path.isdir(ff) and not ff.startswith("_") and "__pycache__" not in package_dir:
            _import_package(base_package + "." + f, ff)
        else:
            _import_module(base_package, ff)


def _import_module(base_package, module_file):
    full_module_name = module_file
    try:
        module_name, ext = os.path.splitext(os.path.split(module_file)[1])
        full_module_name = base_package + "." + module_name
        if ext != ".py":
            return
        if module_name.startswith("_"):
            return
        importlib.import_module(full_module_name)
    except Exception as e:
        log.error(f"module '{full_module_name}' error: {e}")
        sys.exit(1)


def find_registered_method(method_name: str):
    """Вернуть зарегистрированный метод"""
    return _registered_methods.get(method_name, None)
