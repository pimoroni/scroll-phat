#!/usr/bin/env python

# requires: netifaces for looking up IP in readable way
# requires: requests human readable HTTP requests
# requires: geocoder for converting locatio to coords

import os
import json
import time
import urllib
import logging

try:
    from bs4 import BeautifulSoup
except ImportError:
    raise ImportError("This script requires the beautifulsoup4 module")

try:
    import requests
except ImportError:
    raise ImportError("This script requires the requests module")

try:
    import geocoder
except ImportError:
    raise ImportError("This script requires the geocoder module")


import scrollphat


def get_location():
    res = requests.get('http://ipinfo.io')
    if(res.status_code == 200):
        json_data = json.loads(res.text)
        logging.info("Location: {}, {}".format(json_data["city"], json_data["country"]))
        return json_data
    return {}


# Python 2 vs 3 breaking changes.
def encode(qs):
    val = ""
    try:
        val = urllib.urlencode(qs).replace("+", "%20")
    except AttributeError:
        val = urllib.parse.urlencode(qs).replace("+", "%20")
    return val


# Convert a city name and country code to latitude and longitude
def get_coords(address):
    g = geocoder.arcgis(address)
    coords = g.latlng
    logging.info("Location coordinates: %s", coords)
    return coords


# Query Dark Sky (https://darksky.net/) to scrape current weather data
def get_weather(coords):
    weather = {}
    try:
        url = "https://darksky.net/forecast/{}/uk212/en".format(",".join([str(c) for c in coords]))
        logging.info("Requesting weather from: {}".format(url))
        res = requests.get(url)
        if res.status_code == 200:
            soup = BeautifulSoup(res.content, "lxml")
            weather['feelslike'] = soup.find("span", "feels-like-text").text
            weather['high'] = soup.find("span", "high-temp-text").text
            weather['low'] = soup.find("span", "low-temp-text").text
            weather['summary'] = soup.find("span", "summary").text
    except requests.exceptions.RequestException as e:
        logging.error("Could not get weather data from DarkSky: {}".format(e))
        pass

    return weather


def scroll_message(output):
    scrollphat.write_string(output)
    scrollphat.update()

    while(True):
        try:
            scrollphat.scroll()
            scrollphat.update()
            time.sleep(0.2)
        except KeyboardInterrupt:
            return


if(__name__ == '__main__'):
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

    scrollphat.set_brightness(4)
    location = get_location()
    location_string = location["city"] + ", " + location["country"]

    if location.get("city", None) is not None:
        coords = get_coords(location_string)
        weather = get_weather(coords)
        if weather.get("summary", None) is not None:
            print(weather)
            output = "{summary} - L: {low} - H: {high} - Feel: {feelslike}".format(**weather)
            logging.info(output)
            scroll_message(output)

            scrollphat.clear()
            quit()
