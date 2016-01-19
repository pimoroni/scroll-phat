#!/usr/bin/env python

import scrollphat
import math
import time

i = 0
buf = [0] * 11

while True:
    for x in range(0, 11):
        y = (math.sin((i + (x * 10)) / 10.0) + 1) # Produces range from 0 to 2
        y *= 2.5 # Scale to 0 to 5
        buf[x] = 1 << int(y)

    scrollphat.buffer = buf
    scrollphat.update()

    time.sleep(0.005)

    i += 1

