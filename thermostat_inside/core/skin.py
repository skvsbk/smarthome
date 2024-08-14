from time import localtime
from config import st7789py as st7789
from fonts import segment7_32x32 as font_w, segment7_64x64 as font3, freemono_64x64 as font4
from fonts import menlo_rus_16x16 as font_sys
from icons import mqtt_bitmap, wifi_bitmap


def watch(tft):
    now = localtime()
    hours = "{:02d}".format(now[3])
    minutes = "{:02d}".format(now[4])
    tft.write(font_w, hours, 0, 2, st7789.WHITE)
    tft.write(font_w, minutes, 55, 2, st7789.WHITE)
    
    
def mqtt_icon(tft, color):
    mqtt_bitmap.PALETTE[0] = color
    tft.bitmap(mqtt_bitmap, 190, 0)


def wifi_icon(tft, color):
    wifi_bitmap.PALETTE[0] = color
    tft.bitmap(wifi_bitmap, 280, 0)


def inside_temp(tft, temper: float):
    if temper < 18:
        color = st7789.BLUE
    elif temper >=18 and temper < 23:
        color = st7789.GREEN
    else:
        color = st7789.RED
    
    tft.write(font3, str(int(temper // 1)), 5, 70, color)
    tft.write(font3, str(round((temper % 1)*10)), 110, 70, color)
    tft.write(font4, ".", 75, 95, color)


def setpoint_temp(tft, temper: float):
    tft.write(font3, str(int(temper // 1)), 170, 70, st7789.GREEN)
    tft.write(font3, str(round((temper % 1)*10)), 275, 70, st7789.GREEN)
    tft.write(font4, ".", 240, 95, st7789.GREEN)


def outside_temp(tft, temper: int):
    if temper < -5:
        color = st7789.BLUE
    elif temper >=-5 and temper < 10:
        color = st7789.YELLOW
    elif temper >=10 and temper < 23:
        color = st7789.GREEN        
    else:
        color = st7789.RED
    if temper < 0:
        tft.write(font3, str(temper), 2, 175, color)
    else:
        tft.write(font3, " " + str(temper), 2, 175, color)


def forecast(tft, forecast: dict):
    """ "forecast": {
                "forecast_t": "+20..+22",
                "forecast_w": "сильный дождь",
                "forecast_p": "слабый ветер"}"""
  
    tft.write(font_sys, forecast.get("forecast_t"), 155, 170, st7789.WHITE)
    tft.write(font_sys, forecast.get("forecast_w"), 155, 190, st7789.WHITE)
    tft.write(font_sys, forecast.get("forecast_p"), 155, 210, st7789.WHITE)
