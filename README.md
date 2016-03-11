#Scroll pHAT

*Note:* This library is still a little bit beta, we've been rushed off our feet and haven't had time to refine it and come up with a lot of examples. Sorry! It mostly works, though!

11x5 pixels of message scrolling goodness!

https://shop.pimoroni.com/collections/raspberry-pi-zero/products/scroll-phat

#Installing

We've created a super-easy installation script that will install all pre-requisites and get your Scroll pHAT up and running in a jiffy. To run it fire up Terminal which you'll find in Menu -> Accessories -> Terminal on your Raspberry Pi desktop like so:

![Finding the terminal](terminal.jpg)

In the new terminal window type the following and follow the instructions:

```bash
curl -sS get.pimoroni.com/scrollphat | bash
```

If you choose to download examples you'll find them in `/home/pi/Pimoroni/scrollphat`, but you can also check out the examples in this repo: [examples](examples)

# Resetting

To turn off all the LEDs, run the turn_leds_off.py script, or in Python:

```python
import scrollphat
scrollphat.clear()
```
