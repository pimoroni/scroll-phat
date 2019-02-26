#!/usr/bin/env python

import sys
import time

import scrollphat


print("""
Scroll pHAT - Scrolling Text

Press Ctrl+C to exit!

""")

if len(sys.argv) != 2:
    print("""
Usage: {} "message"
""".format(sys.argv[0]))
    sys.exit(0)

scrollphat.set_brightness(2)
scrollphat.write_string(sys.argv[1], 11)

while True:
    try:
        scrollphat.scroll()
        time.sleep(0.1)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
