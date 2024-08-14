"""Device Configuration Module"""
import network
import time
import urequests as request
import socket
import struct
import select
from time import gmtime

from machine import SPI, RTC
import onewire, ds18x20

from .import st7789py as st7789
from .import settings
from fonts import freemono_32x32 as font_wd


########################
#    WIFI
########################
def wifi_check(tft, font, row: int, sta_if):
    """Check Wi-Fi"""
    if sta_if.active and sta_if.isconnected():
        tft.text(font, "Wi-Fi connection established", 10, row * 15, st7789.WHITE, st7789.BLACK)
        return sta_if
    else:
        print("Failed to connect to Wi-Fi")
        tft.text(font, "Failed to connect to Wi-Fi", 10, row*15, st7789.RED, st7789.BLACK)
        tft.text(font, "Fix the problem, then reboot", 10, (row+1)*15, st7789.RED, st7789.BLACK)
        raise 


########################
#    NTP
########################
def get_ntp_time(hrs_offset=0):
    NTP_DELTA = 3155673600 if gmtime(0)[0] == 2000 else 2208988800
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    try:
        addr = socket.getaddrinfo(settings.NTP_HOST, 123)[0][-1]
    except OSError:
        print("NTP socket error")
        return 0
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.settimeout(1)
        s.sendto(NTP_QUERY, addr)
        time.sleep(0.5)
        msg = s.recv(48)
        val = struct.unpack("!I", msg[40:44])[0]  # Can return 0
        return max(val - NTP_DELTA + hrs_offset * 3600, 0)
    except Exception as e:
        print("NTP error s.sendto():", str(e))
    finally:
        s.close()
    return 0  # Timeout or LAN error occurred


def set_time():
    t = get_ntp_time(settings.OFFSET)
    if t == 0:
        print("Can not get ntp time")
        raise OSError
    tm = time.gmtime(t)
    RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))


def ntp_init(tft, font, row: int):
    attempt_connections = 10
    try:
        while attempt_connections > 0:
            set_time()
            attempt_connections -= 1
            time.sleep(0.5)
        tft.text(font, "NTP is synchronized", 10, row*15, st7789.WHITE, st7789.BLACK)
        return None
    except:
        print("NTP is not synchronized")
        tft.text(font, "NTP is not synchronized", 10, row*15, st7789.RED, st7789.BLACK)
        tft.text(font, "Fix the problem, then reboot", 10, (row+1)*15, st7789.RED, st7789.BLACK)
        raise


########################
#    DS18xx
########################
def ds18_check(tft, font, row: int, ds18, room):
    try:
        ds18.convert_temp()
        # First time read 85C
        temp_out = ds18.read_temp(room)
        tft.text(font, "DS18xx is OK (t={:.2f}C)".format(temp_out), 10, row*15, st7789.WHITE, st7789.BLACK)
    except:
        tft.text(font, "DS18xx is not available", 10, row*15, st7789.RED, st7789.BLACK)
        tft.text(font, "Fix the problem, then reboot", 10, (row+1)*15, st7789.RED, st7789.BLACK)
        raise


########################
#    API
########################
def api_check(tft, font, row: int):
    try:
        response = request.get(url=f"{settings.API_SERVER}/probe/?probe_id={settings.PROBE_ID}")
        tft.text(font, "API-server availability is OK", 10, row * 15, st7789.WHITE, st7789.BLACK)
    except:
        print("API-server is not available")
        tft.text(font, "API-server is not available", 10, row * 15, st7789.RED, st7789.BLACK)
        tft.text(font, "Fix the problem, then reboot", 10, (row + 1) * 15, st7789.RED, st7789.BLACK)
        raise


########################
#    Borders
########################
def border(tft, font):
    # Watch devider
    tft.write(font_wd, ":", 38, 10, st7789.WHITE)
    # Current
    tft.rect(0, 50, 155, 85, st7789.WHITE)
    tft.write(font, " Внутри ", 35, 45, st7789.WHITE)
    # Setpoint
    tft.rect(165, 50, 155, 85, st7789.WHITE)
    tft.write(font, " Уставка ", 195, 45, st7789.WHITE)
    # Outside
    tft.rect(0, 155, 320, 85, st7789.WHITE)
    tft.write(font, " За бортом ", 15, 145, st7789.WHITE)
    tft.write(font, " Прогноз ", 175, 145, st7789.WHITE)