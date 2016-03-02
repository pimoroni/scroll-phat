#!/usr/bin/env python

import time
import scrollphat
import socket
import sys
import requests
import json
import urllib

# requires: netifaces for looking up IP in readable way
# requires: requests human readable HTTP requests

def get_location():
    res = requests.get('http://ipinfo.io')
    if(res.status_code == 200):
        json_data = json.loads(res.text)
        return json_data
    return {}

def get_weather(city,country):
    base = "https://query.yahooapis.com/v1/public/yql?"
    query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text=\""+city+", "+country+"\")"
    qs={"q": query, "format": "json", "env": "store://datatables.org/alltableswithkeys"}
    uri = base +  urllib.urlencode(qs).replace("+","%20")
    res = requests.get(uri)
    if(res.status_code==200):
        json_data = json.loads(res.text)
        return json_data
    return {}

location = get_location()
if(location["city"]!=None):
    results = get_weather(location["city"], location["country"])
#    print json.dumps( results )
    for x in range(0, 2):
#	{u'code': u'24', u'text': u'Partly Cloudy/Wind', u'high': u'42', u'low': u'34', u'date': u'2 Mar 2016', u'day': u'Wed'}
        item = results["query"]["results"]["channel"]["item"]["forecast"][x]
        print( item["day"] +": " + item["text"] + " - L: "+ item["low"] + "F - H: "+ item["high"]+"F" )

