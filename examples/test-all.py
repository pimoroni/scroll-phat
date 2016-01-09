#!/usr/bin/env python

import math
import time
import scrollphat
import sys

def millis():
    return int(round(time.time() * 1000))

scrollphat.set_brightness(2)

while True:
    try:
        for x in range(11):
            for y in range(5):
                scrollphat.set_pixel(x,y,1)
                scrollphat.update()
                time.sleep(0.03)
        for x in range(11):
            for y in range(5):
                scrollphat.set_pixel(x,y,0)
                scrollphat.update()
                time.sleep(0.03)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
