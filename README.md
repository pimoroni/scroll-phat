# >>>>>>>>>> Scroll pHAT >>>>>>>>>>

*Note:* This library is still a little bit beta, we've been rushed off our feet and haven't had time to properly test and refine it and come up with examples. Sorry! It mostly works, though!

11x5 pixels of message scrolling goodness!

https://shop.pimoroni.com/collections/raspberry-pi-zero/products/scroll-phat

## Pre-requisites

Use raspi-config to activate i2c

Install the smbus module:

```bash
sudo apt-get install python-smbus
```

If you want to run the sine.py sample you will also need the psutil library:

```bash
sudo apt-get install python-psutil
```

## Installing

You can install the scrollphat library from pip like so:

```bash
sudo pip install scrollphat
```

## Resetting the Scroll pHAT

run the turn_leds_off.py script to turn off all the LEDs

```bash
python turn-leds-off.py
```

