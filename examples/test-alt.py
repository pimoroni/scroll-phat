#!/usr/bin/env python

import math
import sys
import time

import scrollphat


scrollphat.alt_set_brightness(2)


def millis():
    return int(round(time.time() * 1000))

def alt_set_checker(offset):
    n = offset
    for y in range(5):
        for x in range(11):
            scrollphat.alt_set_pixel(x,y,n % 2 == 0)
            n += 1
    scrollphat.alt_update()


while True:
    try:
        scrollphat.alt_set_pixels(lambda x, y: 1, auto_update=True)
        time.sleep(0.5)

        scrollphat.alt_set_pixels(lambda x, y: y % 2 == 0, auto_update=True)
        time.sleep(0.5)

        scrollphat.alt_set_pixels(lambda x, y: x % 2 == 0, auto_update=True) 
        time.sleep(0.5)

        alt_set_checker(0)
        time.sleep(0.5)
        alt_set_checker(1)
        time.sleep(0.5)
    except KeyboardInterrupt:
        scrollphat.alt_clear()
        sys.exit(-1)
