"""Main module"""

from config import settings
from config import st7789py as st7789
from config import initials
from config import globalvars

from core import skin, tasks

from fonts import vga2_8x16 as font_sys
from fonts import menlo_rus_16x16 as font_border

import sys
import time
import asyncio

import machine
import urequests as request


def motion_interrupt(pin):
    globalvars.motion = True


def main():
    # Setup motion detectiom pin
    settings.PIR_IN.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_interrupt)
    # Start line for displaying diagnostics on the screen
    try:
        row = 0
        tft.text(font_sys, "TFT is OK", 10, row*15, st7789.WHITE, st7789.BLACK)
        time.sleep(settings.INIT_SLEEP)
        #
        # Initialize WiFi
        #
        row += 1
        initials.wifi_check(tft=tft, font=font_sys, row=row, sta_if=wlan)
        time.sleep(settings.INIT_SLEEP)
        #
        # Get time from NTP
        #
        row += 1
        initials.ntp_init(tft=tft, font=font_sys, row=row)
        time.sleep(settings.INIT_SLEEP)
        #
        # Check API-server availability
        #
        row += 1
        initials.api_check(tft=tft, font=font_sys, row=row)
        time.sleep(settings.INIT_SLEEP)
        #
        # Initialize sensor DHT/DS18xx
        #
        row += 1
        initials.ds18_check(tft=tft, font=font_sys, row=row, ds18=ds18, room=room)
        time.sleep(settings.INIT_SLEEP)
    except Exception as e:
        print("init failure")
        tft.text(font_sys, f"init failure: {e}", 10, (row+2)*15, st7789.RED, st7789.BLACK)
        tft.text(font_sys, "Fix the problem, then reboot", 10, (row+3)*15, st7789.RED, st7789.BLACK)
        time.sleep(15)
        sys.exit()
    #
    # Clear initialize screen
    #
    tft.fill(st7789.BLACK)
    #
    # Draw borders and titles
    #
    initials.border(tft=tft, font=font_border)
    #
    # Async event loop
    #
    loop = asyncio.get_event_loop()
    
    loop.create_task(tasks.shadow_tft())
    loop.create_task(tasks.ntp_sync())
    loop.create_task(tasks.watch_refresh(tft))
    loop.create_task(tasks.icons_refresh(tft, wlan))
    loop.create_task(tasks.inside_tmp_refresh(tft, ds18, room))
    loop.create_task(tasks.mqtt_pub())
    loop.create_task(tasks.mqtt_sub())
    loop.create_task(tasks.outside_tmp_refresh(tft))
    
    loop.run_forever()




main()
