#!/usr/bin/env python
print("""This example will scroll the words One to Ten
across the ScrollPHAT one at a time using auto-scrolling.

Press Ctrl+C to exit!
""")

import scrollphat

numbers = ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]

try:
    for number in numbers:
        while scrollphat.busy():
            pass
        print("Displaying: {}".format(number))
        scrollphat.write_string(number, scroll=True)

except KeyboardInterrupt:
    scrollphat.stop()
