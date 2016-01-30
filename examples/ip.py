#!/usr/bin/env python

import time
import scrollphat
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
ip = s.getsockname()[0]
s.close()

print(ip)

scrollphat.set_brightness(20)

cpu_values = [0] * 11

while True:
    try:
        scrollphat.clear()
        scrollphat.write_string("IP: " + ip + "    ", 11)
        for i in range(0, scrollphat.buffer_len() - 11):
            scrollphat.scroll()
            time.sleep(0.1)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
