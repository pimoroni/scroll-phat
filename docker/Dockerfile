FROM alexellis2/python-gpio:armv6
# This base image will be fetched automatically from the Docker Hub
# https://hub.docker.com/r/alexellis2/python-gpio/

# For instructions on installing Docker on the PI Zero visit below tutorial
# http://blog.alexellis.io/dockerswarm-pizero/

# Make sure that i2C is enabled on your raspbery pi: sudo raspi-config (interface options / I2C / Yes)

RUN sudo apt-get update && \
    sudo apt-get -qy install python-smbus i2c-tools psutil

ADD ./examples  ./examples
ADD ./library   ./library
ADD ./tools     ./tools

RUN cd library && \
    python setup.py install

CMD ["python"]
