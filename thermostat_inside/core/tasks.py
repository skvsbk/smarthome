"""Async tasks module"""

import asyncio
import ujson

from .import skin
from config import initials, settings, globalvars
from config import st7789py as st7789


async def ntp_sync():
    await asyncio.sleep(3600)
    while True:
        initials.set_time()
        await asyncio.sleep(3600)


async def watch_refresh(tft):
    while True :
        skin.watch(tft=tft)
        await asyncio.sleep(5)


async def icons_refresh(tft, wlan):
    while True:
        try:
            wlan_level = wlan.status("rssi")
#             print("WiFi Level", wlan_level)
            if wlan_level >= - 50:
                wifi_icon_color = st7789.GREEN
            elif wlan_level < -50 and wlan_level >=-75:
                wifi_icon_color = st7789.YELLOW
            else:
                wifi_icon_color = st7789.RED
        except:
            wifi_icon_color = st7789.RED

        skin.wifi_icon(tft=tft, color=wifi_icon_color)
        skin.mqtt_icon(tft=tft, color=st7789.GREEN)
        await asyncio.sleep(15)


async def inside_tmp_refresh(tft, ds18, room):
    while True:
        ds18.convert_temp()
        globalvars.temperatute = ds18.read_temp(room)
        skin.inside_temp(tft=tft, temper=globalvars.temperatute)
        await asyncio.sleep(3)


async def shadow_tft():
    while True:
        if globalvars.motion:
            settings.BACKLIGHT.on()
            await asyncio.sleep(settings.BACKLITE_TIME)
            settings.BACKLIGHT.off()
            globalvars.motion = False
        await asyncio.sleep(1)


async def outside_tmp_refresh(tft):
    while True:
        if globalvars.setpoint:
            skin.setpoint_temp(tft=tft, temper=globalvars.setpoint)
            globalvars.setpoint = None
        if globalvars.outside_t:
            skin.outside_temp(tft=tft, temper=globalvars.outside_t)
            globalvars.outside_t = None
        if globalvars.forecast:
            skin.forecast(tft=tft, forecast=globalvars.forecast)
            globalvars.forecast = None
        await asyncio.sleep(2)


async def mqtt_pub():
    # send T by MQTT
    while True:
        msg = {
            "probe_id": settings.PROBE_ID,
            "temperatute": globalvars.temperatute
        }
        print("mqtt_pub", ujson.dumps(msg))
        await asyncio.sleep(15)


async def mqtt_sub():
    # Get outside temp, setpoint and weather forecast
    while True:
        msg = """{
            "setpoint": 23.4,
            "outside_t": 24,
            "forecast": {
                "forecast_t": "+20..+22",
                "forecast_w": "сильный дождь",
                "forecast_p": "слабый ветер"}
            }"""
        msg_json = ujson.loads(msg)
        globalvars.setpoint = msg_json.get("setpoint")
        globalvars.outside_t = msg_json.get("outside_t")
        globalvars.forecast = msg_json.get("forecast")
        await asyncio.sleep(1)
