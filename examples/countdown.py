import datetime
import time
import scrollphat

try:
    print("Please enter the target time with integers")
    year = input("Year:\t")
    month = input("Month:\t")
    d = input("Date:\t")
    h = input("Hour:\t")
    m = input("Minute:\t")


    while 1:
        delta = datetime.datetime(int(year), int(month), int(d), int(h), int(m)) - datetime.datetime.now()
        deltaSec = int(delta.total_seconds())
        deltaMin = int(delta.total_seconds() // 60)
        deltaHour = int(delta.total_seconds() // 3600)

        if deltaMin > 99 and deltaHour < 99:
            dis = str(deltaHour) + "h"
            scrollphat.write_string(dis)
            time.sleep(60)
            scrollphat.clear()
        elif deltaSec > 999 and deltaMin <= 99:
            dis = str(deltaMin) + "\""
            scrollphat.write_string(dis)
            time.sleep(2.5)
            scrollphat.clear()
        elif 0 <= deltaSec <= 999:
            dis = str(deltaSec)
            scrollphat.write_string(dis)
            time.sleep(0.25)
            scrollphat.clear()
        elif deltaSec < 0:
            for x in range(11):
                for y in range(5):
                    scrollphat.set_pixel(x,y,1)
            scrollphat.update()
            while 1: #DISPLAY FLASH
                scrollphat.set_brightness(0)
                time.sleep(1)
                scrollphat.set_brightness(10)
                time.sleep(1)
        else:
            print("Cannot display: Out of range.")
            scrollphat.clear()
            exit()
except KeyboardInterrupt:
    scrollphat.clear()
