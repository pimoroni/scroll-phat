#!/usr/bin/env python

import sys
import time

import scrollphat


print("""
Scroll pHAT - Scroll Text, Once.
""")

scrollphat.set_brightness(2)

if len(sys.argv) != 2:
    print("""
Usage: {} "message"

""".format(sys.argv[0]))
    sys.exit(0)

scrollphat.write_string(sys.argv[1], 11)
length = scrollphat.buffer_len()

for i in range(length):
    try:
        scrollphat.scroll()
        time.sleep(0.1)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
