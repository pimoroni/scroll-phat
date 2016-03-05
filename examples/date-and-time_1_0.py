##!/usr/bin/env python
import scrollphat
import sys
import time

while True:

	try:
		dayNumber = time.strftime("%d")
	
		if dayNumber == ("01","21","31"):
			suffix = "st"
		if dayNumber == ("02","22"):
			suffix = "nd"
		if dayNumber == ("03","23"):
			suffix = "rd"
		else:
			suffix = "th"
	
		dayName = time.strftime("%A")
		dayNumberShort = dayNumber.lstrip("0")
		month = time.strftime("%B")
		year = time.strftime("%Y")
		hour = time.strftime("%H")
		minutes = time.strftime("%M")
		seconds = time.strftime("%S")
	
		assembledDateString = dayName + " " + dayNumberShort + suffix + " " + month + " " + year + "    " + hour + ":" + minutes + ":" + seconds + "    "

		scrollphat.rotate = True
		scrollphat.set_brightness(10)
	
		scrollphat.write_string(assembledDateString)
		scrollphat.scroll()
		time.sleep(0.1)
	
	except KeyboardInterrupt:
		scrollphat.clear()
		sys.exit(-1)
