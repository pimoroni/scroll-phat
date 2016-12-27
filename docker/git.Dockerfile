FROM resin/rpi-raspbian
MAINTAINER alexellis2@gmail.com

ENTRYPOINT []

WORKDIR /root/

RUN apt-get update \
    && apt-get install git python-dev python-smbus i2c-tools python-pip gcc \
    && git clone https://github.com/pimoroni/scroll-phat \
    && cd scroll-phat/library && python setup.py install \
    && apt-get -qy remove python-dev gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root/scroll-phat/examples

CMD ["python"]

