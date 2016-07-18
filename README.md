![Scroll pHAT](scroll-phat-logo-new.png)

11x5 pixels of single-colour, message scrolling goodness!

https://shop.pimoroni.com/products/scroll-phat

#Installing

We've created a super-easy installation script that will install all pre-requisites and get your Scroll pHAT up and running in a jiffy. To run it fire up Terminal which you'll find in Menu -> Accessories -> Terminal on your Raspberry Pi desktop like so:

![Finding the terminal](terminal.jpg)

In the new terminal window type the following and follow the instructions:

```bash
curl -sS https://get.pimoroni.com/scrollphat | bash
```

If you choose to download examples you'll find them in `/home/pi/Pimoroni/scrollphat`, but you can also check out the examples in this repo: [examples](examples)

# Docker image

For those who are curious and interested in learning about Docker and the PI, this repository includes a fully tested Dockerfile for using the scrollphat library without needing to install it on the base system.

To build, cd into the docker directory and run:

```
$ ./build_docker.sh
```

For complete instructions, see DOCKER.md in the same directory.
