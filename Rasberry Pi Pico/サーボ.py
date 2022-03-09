from machine import PWM,Pin
import time

led=Pin(25,Pin.OUT)

servoharu=PWM(Pin(0))
servoharu.freq(50)

max_duty=65535

kakudo_0=0.0725
kakudo_90=0.12

while True :
    led.toggle()
    servoharu.duty_u16(int(max_duty*kakudo_0))
    time.sleep(1)
    led.toggle()
    servoharu.duty_u16(int(max_duty*kakudo_90))
    time.sleep(1)

