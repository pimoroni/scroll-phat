FROM resin/rpi-raspbian
MAINTAINER alexellis2@gmail.com
ENTRYPOINT []

RUN mkdir -p /root/scroll-phat
WORKDIR /root/scroll-phat/

RUN apt-get update \
    && apt-get install \
       python-dev \
       python-smbus \
       i2c-tools \
       python-pip \
       gcc

COPY ./examples  ./examples
COPY ./library   ./library
COPY ./tools     ./examples

RUN cd library && python setup.py install

CMD ["python"]
