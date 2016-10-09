#!/usr/bin/env python

import sys
import time

import scrollphat


scrollphat.set_brightness(2)
scrollphat.clear()

try:
    scrollphat.alt_set_brightness(2)
    scrollphat.alt_clear()
except:
    sys.exit("can't find second Scroll pHAT on i2c0 bus!")

if len(sys.argv) != 2:
    print("\nusage: python simple-text-scroll.py \"message\" \npress CTRL-C to exit\n")
    sys.exit(0)

while True:
    scrollphat.write_string(sys.argv[1] + "    ", 22)
    scrollphat.alt_write_string(sys.argv[1] + "    ", 11)
    travel = scrollphat.buffer_len() - 11

    try:
        for i in range(travel):
            scrollphat.alt_scroll()
            scrollphat.scroll()
            time.sleep(0.1)
        scrollphat.clear()
        scrollphat.alt_clear()
    except KeyboardInterrupt:
        scrollphat.clear()
        scrollphat.alt_clear()
        sys.exit(-1)
