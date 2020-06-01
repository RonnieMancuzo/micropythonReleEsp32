import machine
import time

r = machine.Pin(2, machine.Pin.OUT)

while True:
    r.value(0)
    time.sleep(5)
    r.value(1)
    time.sleep(5)