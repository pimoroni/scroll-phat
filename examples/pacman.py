import time
import scrollphat as sf
import sys

sf.set_rotate(True)
sf.set_brightness(30)

while (True):
    try:
        # pacman ani 1
        for i in range(7,10):
            sf.set_pixel(i, 0, True)
        for i in range(6,9):
            sf.set_pixel(i, 1, True)
        for i in range(9,11):
	    sf.set_pixel(i, 1, False)
	for i in range(6,8):
            sf.set_pixel(i, 2, True)
	sf.set_pixel(8,2, False)
        for i in range(6,9):
            sf.set_pixel(i, 3, True)
	for i in range(9,11):
            sf.set_pixel(i, 3, False)
        for i in range(7,10):
            sf.set_pixel(i, 4, True)
	# ghost ani 1
	for i in range(1,4):
            sf.set_pixel(i, 0, True)
        for i in range(0,5):
            sf.set_pixel(i, 1, True)
        sf.set_pixel(1,1, False)
        sf.set_pixel(3,1, False)
        for i in range(0,5):
            sf.set_pixel(i, 2, True)
        for i in range(0,5):
            sf.set_pixel(i, 3, True)
        for i in range(0,5):
            sf.set_pixel(i, 4, True)
        sf.set_pixel(1,4, False)
        sf.set_pixel(3,4, False)
	# update this ani
       	sf.update()
        time.sleep(.15)
	# pacman ani 2
        for i in range(6,11):
            sf.set_pixel(i, 1, True)
        for i in range(6,9):
            sf.set_pixel(i, 2, True)
        for i in range(6,11):
            sf.set_pixel(i, 3, True)
	# ghost ani 2
        for i in range(0,5):
            sf.set_pixel(i, 4, True)
        sf.set_pixel(0,4, False)
        sf.set_pixel(2,4, False)
        sf.set_pixel(4,4, False)
	# update this ani
        sf.update()
        time.sleep(.15)
	# pacman ani 3
        for i in range(6,11):
            sf.set_pixel(i, 2, True)
	# ghost ani 3
        for i in range(0,3):
            sf.set_pixel(i, 4, True)
        sf.set_pixel(1,4, False)
	# update this ani
	sf.update()
        time.sleep(.15)
        # pacman ani 4 
        for i in range(9,11):
	    sf.set_pixel(i, 2, False)
	# ghost ani 4
        for i in range(2,5):
            sf.set_pixel(i, 4, True)
        sf.set_pixel(3,4, False)
	# update this ani
        sf.update()
        time.sleep(.15)
    except KeyboardInterrupt:
	sf.clear()
        sys.exit(-1)
