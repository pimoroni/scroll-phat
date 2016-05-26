import scrollphat as sp
import time

sp.set_brightness(64)

while True:
    print("0 to 5")
    sp.graph([0,1,2,3,4,5])
    time.sleep(1.0)
    sp.clear()
    print("0 to 10")
    sp.graph([0,2,4,6,8,10])
    time.sleep(1.0)
    sp.clear()

