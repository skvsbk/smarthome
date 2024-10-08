"""Модуль получения погоды"""

import requests
from bs4 import BeautifulSoup
from config.settings import URL_WEATHER
from core.method import register_method

"""
Request
{
    "method": "m_weather_get",
    "parameters": []
}

Response
{
    "weather": {
        "temperature": "+8..+7",
        "precipitation": "без осадков",
        "wind": "легкий ветер",
    }
}
"""

@register_method(method_name="m_weather_get")
async def m_weather_get():
    """Метод получения значение погоды"""
    temperature, precipitation, wind = rp5_weather_get()
    return {"weather": [
        {"temperature": temperature},
        {"precipitation": precipitation},
        {"wind": wind}]
    }


def rp5_weather_get() -> tuple:
    """Парсинг сайта погоды rp5.ru"""
    page = requests.get(URL_WEATHER)
    soup = BeautifulSoup(page.text, "html.parser")
    tag_b = soup.find("div", id="forecastShort-content").find("b").text
    tag_b_split = tag_b.split(". ")[0].split(",")
    temperature = tag_b.split(" ")[2]
    precipitation = tag_b_split[2].strip()
    wind = tag_b_split[3].strip()
    return temperature, precipitation, wind


if __name__ == '__main__':
    rp5_weather_get()
