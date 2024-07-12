Термостат комнатный, с дисплеем

Оборудование:
MB:	ESP32-WROOM-32D		https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32d_esp32-wroom-32u_datasheet_en.pdf
TFT:	ST7789 SPI 240x320	https://aliexpress.ru/item/4001282467099/reviews?filters=&sku_id=12000017591977476
DHT:	DHT			...


Коммутация:
ESP32		TFT
GPIO19		SDO(MISO)
GPIO-		LED
GPIO18		SCK
GPIO23		SDI(MOSI)
GPIO2		DC
GPIO4		RESET
GPIO5		SC

		DHT
GPIO		D

Библиотеки:
Драйвер	https://github.com/russhughes/st7789py_mpy/blob/master/lib/st7789py.py
Шрифты	