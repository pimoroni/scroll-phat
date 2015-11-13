import math
import time
import scrollphat

def millis():
    return int(round(time.time() * 1000))

while True:
    buf = [0] * 11
    t = millis()/50
    for o_x in range(11):
        x = t + (o_x/3.0)
        y = int((math.sin(x) + 1) * 2.5)
        buf[o_x] |= (1 << y)
    scrollphat.update(buf)
