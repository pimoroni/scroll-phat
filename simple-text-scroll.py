import scrollphat
import sys
import time

if len(sys.argv) != 2:
    print "\nusage: python simple-text-scroll.py \"message\" \npress CTRL-C to exit\n"
    sys.exit(0)

scrollphat.write_string(sys.argv[1] + "   ")

while True:
    scrollphat.scroll()
    time.sleep(0.1)
