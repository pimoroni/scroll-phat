FROM alexellis2/python-gpio:armv6
# This base image will be fetched automatically from the Docker Hub
# https://hub.docker.com/r/alexellis2/python-gpio/

# For instructions on installing Docker on the Pi visit the below tutorial:
# http://blog.alexellis.io/hands-on-docker-raspberrypi/

# i2c must be enabled on the Pi's host OS - through the `curl | sh` script in
# the root of the repository or through raspi-config (if using Raspbian)

RUN apt-get update && \
    apt-get -qy install python-smbus i2c-tools

ADD ./examples  ./examples
ADD ./library   ./library
ADD ./tools     ./tools

RUN cd library && \
    python setup.py install

CMD ["python"]
