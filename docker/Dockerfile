FROM alexellis2/python-gpio:armv6
# This base image will be fetched automatically from the Docker Hub
# https://hub.docker.com/r/alexellis2/python-gpio/

# For instructions on installing Docker on the PI Zero visit below tutorial
# http://blog.alexellis.io/dockerswarm-pizero/

RUN apt-get update && \
    apt-get -qy install python-smbus i2c-tools

ADD ./examples  ./examples
ADD ./library   ./library
ADD ./tools     ./tools

RUN cd library && \
    python setup.py install

CMD ["python"]
