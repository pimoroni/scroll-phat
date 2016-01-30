#!/usr/bin/env python

import time
import scrollphat
import socket
import sys
import requests
import json

# requires: netifaces for looking up IP in readable way
# requires: requests human readable HTTP requests

# Retrieve and print either the public IP or an internal IP address for an
# adapter such as wlan0 by passing it as an argument to the program.
# sudo python wlan0 => 192.168.0.x (useful for wifi hotspots)

def get_internal_ip(interface):
    ip = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1]
    return ip

def get_public_ip():
    res = requests.get('http://ipinfo.io')
    if(res.status_code == 200):
        json_data = json.loads(res.text)

        # this reponse also contains rich geo-location data
        ip = json_data['ip']
    else:
        return "127.0.0.1"

def get_ip(mode):
    ip = "127.0.0.1"
    if(mode == "public"):
        ip = get_public_ip()
    else:
        ip = get_internal_ip(mode)
    return ip
    
address_mode = "public"
if(len(sys.argv) == 2):
    address_mode = sys.argv[1]

ip = get_ip(address_mode)

print(address_mode + " IP Address: " +str(ip))

scrollphat.set_brightness(20)

while True:	
    scrollphat.clear()
    scrollphat.write_string("IP: " + ip + "    ", 11)
    for i in range(0, scrollphat.buffer_len() - 11):
        scrollphat.scroll()
        time.sleep(0.1)

