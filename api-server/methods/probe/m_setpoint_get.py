"""Модуль получения уставки"""

from core.executor import MethodParams
from core.method import register_method
from methods.crud.setpoint import setpoint_get


# Request
# {
#     "method": "m_setpoint_get",
#     "parameters": [
#         {
#             "name": "probe_id",
#             "type": "bigint",
#             "bigint": 2
#         }
#     ]
# }
#
# Response
# {
#     "setpoint": {
#         "id": 1,
#         "probe_id": 2,
#         "t2": null,
#         "l1": null,
#         "t1": 22.0,
#         "t3": null,
#         "l2": null
#     }
# }

@register_method(method_name="m_setpoint_get")
async def m_setpoint_get(params: MethodParams):
    """Метод получения значения уставки"""
    probe_id = params.get("probe_id")
    setpoint = setpoint_get(db=params.db, probe_id=probe_id)
    return {"setpoint": setpoint}
