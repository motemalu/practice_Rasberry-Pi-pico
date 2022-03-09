from machine import Pin
import utime

led_green=Pin(16,Pin.OUT)
led_yellow=Pin(17,Pin.OUT)
led_red=Pin(18,Pin.OUT)

while True :
    led_green.value(1)
    utime.sleep(5)
    led_green.value(0)
    led_yellow.value(1)
    utime.sleep(1)
    led_yellow.value(0)
    led_red.value(1)
    utime.sleep(3)
    led_red.value(0)


