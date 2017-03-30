![Scroll pHAT](scroll-phat-logo-new.png)
https://shop.pimoroni.com/products/scroll-phat

11x5 pixels of single-colour, message scrolling goodness!

## Installing

### Full install (recommended):

We've created an easy installation script that will install all pre-requisites and get your Scroll pHAT
up and running with minimal efforts. To run it, fire up Terminal which you'll find in Menu -> Accessories -> Terminal
on your Raspberry Pi desktop, as illustrated below:

![Finding the terminal](http://get.pimoroni.com/resources/github-repo-terminal.png)

In the new terminal window type the command exactly as it appears below (check for typos) and follow the on-screen instructions:

```bash
curl https://get.pimoroni.com/scrollphat | bash
```

Alternatively, on Raspbian, you can download the `pimoroni-dashboard` and install your product by browsing to the relevant entry:

```bash
sudo apt-get install pimoroni
```
(you will find the Dashboard under 'Accessories' too, in the Pi menu - or just run `pimoroni-dashboard` at the command line)

If you choose to download examples you'll find them in `/home/pi/Pimoroni/scrollphat/`.

### Manual install:

#### Library install for Python 3:

on Raspbian:

```bash
sudo apt-get install python3-scrollphat
```

other environments: 

```bash
sudo pip3 install scrollphat
```

#### Library install for Python 2:

on Raspbian:

```bash
sudo apt-get install python-scrollphat
```

other environments: 

```bash
sudo pip2 install scrollphat
```

### Development:

If you want to contribute, or like living on the edge of your seat by having the latest code, you should clone this repository, `cd` to the library directory, and run:

```bash
sudo python3 setup.py install
```
(or `sudo python setup.py install` whichever your primary Python environment may be)

In all cases you will have to enable the i2c bus.

## Documentation & Support

* Guides and tutorials - https://learn.pimoroni.com/scroll-phat
* Function reference - http://docs.pimoroni.com/scrollphat/
* GPIO Pinout - https://pinout.xyz/pinout/scroll_phat
* Get help - http://forums.pimoroni.com/c/support

## Docker image

For those who are curious and interested in learning about Docker on the Pi, this repository includes a fully tested Dockerfile for using the scrollphat library without needing to install it on the base system.

To build, cd into the docker directory and run:

```
$ ./build_docker.sh
```

For complete instructions, see DOCKER.md in the same directory.
