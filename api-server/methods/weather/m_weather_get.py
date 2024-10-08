"""Модуль получения погоды"""

import requests
from bs4 import BeautifulSoup
from config.settings import URL_WEATHER
from core.executor import MethodParams
from core.method import register_method
from core.utils import get_logger

log = get_logger(__name__)

# Request
# {
#     "method": "m_weather_get",
#     "parameters": []
# }
#
# Response
# {
#     "weather": {
#         "temperature": "+8..+7",
#         "precipitation": "без осадков",
#         "wind": "легкий ветер",
#     }
# }


@register_method(method_name="m_weather_get")
async def m_weather_get(params: MethodParams):
    """Метод получения значение погоды"""
    try:
        temperature, precipitation, wind = rp5_weather_get()
        return {"weather": [
            {"temperature": temperature},
            {"precipitation": precipitation},
            {"wind": wind}]
        }
    except ValueError as e:
        log.error(str(e))
        return {"error": str(e)}


def rp5_weather_get() -> tuple:
    """Парсинг сайта погоды rp5.ru"""
    page = requests.get(URL_WEATHER, timeout=30)
    if page.status_code != 200:
        raise ValueError("Timeout expired")
    soup = BeautifulSoup(page.text, "html.parser")
    tag_b = soup.find("div", id="forecastShort-content").find("b").text
    tag_b_split = tag_b.split(". ")[0].split(",")
    temperature = tag_b.split(" ")[2]
    precipitation = tag_b_split[2].strip()
    wind = tag_b_split[-1].strip()
    return temperature, precipitation, wind


if __name__ == '__main__':
    rp5_weather_get()
