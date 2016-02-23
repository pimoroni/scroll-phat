#!/usr/bin/env python
print("""This example will scroll the supplied message
on your Scroll pHAT using asyncronous scrolling.""")

import scrollphat
import sys

if len(sys.argv) < 2:
    print("\nUsage: python auto-scroll.py \"message\" <repeat_count>")
    sys.exit(0)

message = sys.argv[1]
repeat = 1

if len(sys.argv) > 2:
    repeat = int(sys.argv[2])

scrollphat.write_string(message,
                        scroll=True,      # Turn auto scrolling on
                        repeat=repeat,    # Number of times to repeat
                        delay=0.1,        # Number of seconds between shifts
                        repeat_delay=0.2  # Number of seconds between repeats
                       )

print("\nDisplaying {message}, {repeat} times.".format(message=message, repeat=repeat))
print("\nPress Ctrl+C to exit.")

try:
    while scrollphat.busy():
        pass
    print("\nDone!\n")

except KeyboardInterrupt:
    print("\nStopping...\n")
    scrollphat.stop()
    scrollphat.clear()
