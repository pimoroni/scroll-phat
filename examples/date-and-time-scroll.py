#!/usr/bin/env python
# Script to display date and time, i.e.:
import sys
import time
import scrollphat

scrollphat.clear()    # Clear pHAT display ensuring nothing is displayed prior to starting

while True:
    try:
        dNumLng = time.strftime("%d")  # Long day with any leading zeroes
        dNum = dNumLng.lstrip("0")     # Strip leading zeroes, if any

        def get_day_sufx(dNum):        # Work out "st", "nd", "rd" or "th"
            if dNum == ("1","21","31"):
                return "st"
            if dNum == ("2","22"):
                return "nd"
            if dNum == ("3","23"):
                return "rd"
            else:
                return "th"

        sufx = get_day_sufx(dNum)   # Run above, supply date, create suffix
        dNam = time.strftime("%A")  # Day name
        mnth = time.strftime("%B")  # Month name (full)
        year = time.strftime("%Y")  # Year (4 digits)
        hour = time.strftime("%H")  # Hours (24 hours)
        mins = time.strftime("%M")  # Minutes
        secs = time.strftime("%S")  # Seconds

        # Assemble all the variables into a single string
        assembled = " " + dNam + " " + dNum + sufx + " " + mnth + " " + year + "    " + hour + ":" + mins + ":" + secs + "    "

        scrollphat.set_brightness(10)      # Readable brightness?
        scrollphat.write_string(assembled) # Create the string for the pHAT
        scrollphat.scroll()                # Scroll the string
        time.sleep(0.1)                    # Control the speed

    except KeyboardInterrupt: # Stop script if "Ctrl+C" is pressed
        scrollphat.clear()    # Clear pHAT display before exiting
        sys.exit(-1)
