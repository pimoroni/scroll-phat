#!/usr/bin/env python

import sys
import time

import scrollphat


print("""
Scroll pHAT - Scroll Text Quickstart

Super basic example of srolling text.

Press Ctrl+C to exit!

""")

scrollphat.set_brightness(2)

if len(sys.argv) != 2:
    print("""
Usage: python {} "message"
""".format(sys.argv[0]))
    sys.exit(0)

scrollphat.write_string(sys.argv[1] + "    ")

while True:
    try:
        scrollphat.scroll()
        time.sleep(0.1)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
