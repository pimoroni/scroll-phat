#!/usr/bin/env python

import scrollphat
import sys
import time

if len(sys.argv) != 2:
    print("\nusage: python simple-text-scroll-rotated.py \"message\" \npress CTRL-C to exit\n")
    sys.exit(0)

scrollphat.set_rotate(True)
scrollphat.write_string(sys.argv[1] + "   ")

while True:
    try:
        scrollphat.scroll()
        time.sleep(0.1)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
