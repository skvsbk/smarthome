"""Константы проекта"""
from machine import Pin

########################
#    Initial params
########################
INIT_SLEEP = 0
########################
#    System params
########################
PROBE_ID = 1
API_SERVER = "http://10.0.2.115:8000"

########################
#    Wi-Fi
########################
SSID = "AnyaKotya"
PASS = "24061805"
########################
#    NTP
########################
NTP_HOST = "10.0.2.115"  #"10.0.2.115"  # "ntp1.ntp-servers.net"  #
OFFSET = 3
########################
#    TFT
########################
SPI_ID = 2
BAUDRATE = 20000000
SCK = Pin(18)
MOSI = Pin(23)
MISO = Pin(19)
TFT_WIDTH = 240
TFT_HEIGHT = 320
RESET = Pin(4, Pin.OUT)
CS = Pin(5, Pin.OUT)
DC = Pin(2, Pin.OUT)
BACKLIGHT = Pin(27, Pin.OUT)
INVERSION_MODE = None
ROTATION = 1
########################
#    DHT/DS18x
########################
DHT_IN = Pin(14)
########################
#    PIR sensor AM312
########################
PIR_IN = Pin(12, Pin.IN)
BACKLITE_TIME = 60
