![Scroll pHAT](scroll-phat-logo-new.png)

11x5 pixels of single-colour, message scrolling goodness!

https://shop.pimoroni.com/products/scroll-phat

#Installing

**Full install ( recommended ):**

We've created a super-easy installation script that will install all pre-requisites and get your Scroll pHAT up and running in a jiffy. To run it fire up Terminal which you'll find in Menu -> Accessories -> Terminal on your Raspberry Pi desktop like so:

![Finding the terminal](terminal.jpg)

In the new terminal window type the following and follow the instructions:

```bash
curl -sS https://get.pimoroni.com/scrollphat | bash
```

If you choose to download examples you'll find them in `/home/pi/Pimoroni/scrollphat/`.

**Library install for Python 3:**

on Raspbian:

```bash
sudo apt-get install python3-scrollphat
```
other environments: 

```bash
sudo pip3 install scrollphat
```

**Library install for Python 2:**

on Raspbian:

```bash
sudo apt-get install python-scrollphat
```
other environments: 

```bash
sudo pip2 install scrollphat
```

In all cases you will have to enable the i2c bus.

# Docker image

For those who are curious and interested in learning about Docker and the PI, this repository includes a fully tested Dockerfile for using the scrollphat library without needing to install it on the base system.

To build, cd into the docker directory and run:

```
$ ./build_docker.sh
```

For complete instructions, see DOCKER.md in the same directory.
