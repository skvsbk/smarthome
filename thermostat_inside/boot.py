# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()


import network, gc, time
import onewire, ds18x20
from config import settings, st7789py as st7789
from machine import SPI


def wifi_init():
    """Initialize Wi-Fi"""
    try:
        sta_if = network.WLAN(network.STA_IF)
        sta_if.active(True)
        time.sleep(0.5)
        sta_if.connect(settings.SSID, settings.PASS)
        while not sta_if.isconnected():
            time.sleep(0.1)
    except:
        print("Failed to active Wi-Fi. Please reboot.")
        return None
    return sta_if


def tft_init(rotation=0):
    """
    Configures and returns an instance of the ST7789 display driver.
    Args:
        rotation (int): The rotation of the display (default: 0).
    Returns:
        ST7789: An instance of the ST7789 display driver.
    """
    return st7789.ST7789(
        SPI(settings.SPI_ID, baudrate=settings.BAUDRATE, sck=settings.SCK, mosi=settings.MOSI, miso=settings.MISO),
        settings.TFT_WIDTH,
        settings.TFT_HEIGHT,
        reset=settings.RESET,
        cs=settings.CS,
        dc=settings.DC,
        backlight=settings.BACKLIGHT,
        rotation=rotation)


def ds18_init():
    try:
        ds18 = ds18x20.DS18X20(onewire.OneWire(settings.DHT_IN))
        rooms = ds18.scan()
        return ds18, rooms[0]
    except:
        return None, None 


wlan = wifi_init()
print(wlan.ifconfig())
print("WiFi level", wlan.status("rssi"))

tft = tft_init(settings.ROTATION)
tft.inversion_mode(None)
tft.fill(st7789.BLACK)

ds18, room = ds18_init()
gc.collect()
