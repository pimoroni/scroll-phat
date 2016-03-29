#!/usr/bin/env python
"""
Little http server that makes the scrollphat examples 
accessable over the web, and adds adjustable brightness,
update time and rotation for some of them.

Works for both IPv4 and IPv6, running on either python 2 or 3

Author: Joost Witteveen (joosteto@gmail.com)
The text, sine and CPU scrollphat routines are from the scrollphat examples.
"""
import sys
if sys.version_info >= (3,0):
    #Python3:
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib import parse as urlparse
    def bytes_(m,c): return bytes(m,c)
else:
    #Python2:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
    import urlparse
    def bytes_(m,c): return bytes(m)
try:
    import scrollphat
    dummy=False
except ImportError:
    print("scrollphat module could not be imported, will run in dummy mode")
    dummy=True
from multiprocessing import Process
import time
import math
import psutil
import socket
try:
    import life
except ImportError:
    print("life.py module not found, 'game of life' will not work") 

def do_scroll(stype, dorotate, text, brightness=20, delay=0.2):
    def scroll_text(delay, text):
        scrollphat.write_string(text)
        while True:
            scrollphat.scroll()
            time.sleep(delay)
        
    def scroll_sine(delay):
        i=0
        buf=[0]*11
        while True:
            for x in range(0, 11):
                y = (math.sin((i + (x * 10)) / 10.0) + 1) # Produces range from 0 to 2
                y *= 2.5 # Scale to 0 to 5
                buf[x] = 1 << int(y)
    
            scrollphat.set_buffer(buf)
            scrollphat.update()
    
            time.sleep(delay)
            i += 1

    def scroll_cpu(delay):
        cpu_values = [0] * 11
        while True:
            cpu_values.pop(0)
            cpu_values.append(psutil.cpu_percent())
            
            scrollphat.graph(cpu_values, 0, 25)
            time.sleep(delay)

    if dummy:
        return
    scrollphat.set_brightness(brightness)
    scrollphat.set_rotate(dorotate)
    if stype in "text":
        scroll_text(delay, text)
    elif stype == ("cpu"):
        scroll_cpu(delay)
    elif stype=="sine":
        scroll_sine(delay)
    elif stype=="life":
        life.scroll_life(delay=delay)
    else:
        #Ugly, but the only way to make these examples work, as
        #they lack the 'if __name__ == "__main__"' magic.
        #This also means update time and brightness don't work for most.
        __import__(stype)

        
scroll_process=None
def start_scroll_thread(stype="text", dorotate=False, text='SCROLLPHAT\_/^--', brightness=20, delay=0.2):
    #do_scroll(stype, dorotate, text, brightness, delay)
    global scroll_process
    if scroll_process!=None:
        scroll_process.terminate()
    scroll_process=Process(target=do_scroll, args=(stype, dorotate, text, brightness, delay))
    scroll_process.start()

class HTTPServerV6(HTTPServer):
    #This makes the server work for both IPv4 and IPv6:
    address_family = socket.AF_INET6
  
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query=urlparse.parse_qs(urlparse.urlparse(self.path).query)
        text="SCROLLPHAT\_/^--"
        stype=query.get('type', ["sine"])[0]
        brightnessstr = query.get('brightness', ["63"])[0]
        updatestr=query.get('update', ["0.1"])[0]
        dorotate=query.get('orientation', [""])[0] == "rot"
        errstr=""
        if dummy:
            errstr+="WARNING: could not import scrollphat module, running in dummy mode<br>"
        if len(query.keys()):
            text=query.get('text', [""])[0]
            try:
                brightness=int(brightnessstr)
            except ValueError:
                errstr+="Error: brightness should be an integer, not \"{0}\"<br>".format(brightnessstr)
            try:
                update=float(updatestr)
            except ValueError:
                errstr+="Error: update time should be a floating point number, not \"{0}\"<br>".format(updatestr)
            start_scroll_thread(stype, dorotate, text, brightness, update)
    
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        radiostr=""
        for ty, desc in  [("text", "Text (enter text below)"),  ("sine", "Sine"),
                          ("life", '<a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life">Life</a>'),
                          ("cpu", "CPU"), ("test-all", "Test All LEDs"),
                          ("ip", "IP"), ("progress", "Progress"),
                          ("ukweather", "UK Weather"), ("uptime", "Uptime"),
                          ("binary-clock", "Binary Clock"),
                          ("localweather", "Local weather")]:
            radiostr+='<input type="radio" name="type" value="{ty}" {checked}>{desc}<br>\n'.format(
                ty=ty, desc=desc, checked=["", "checked"][stype==ty])
        self.wfile.write(bytes_("""
<h1>Scroll Phat Server</h1>
<p style="color:red">{errstr}</p>
<form>
    Brightness (0--127):
    <input type="text" name="brightness" value="{brightness}"><br>
    Update time (seconds):
    <input type="text" name="update" value="{update}"><br>
    <input type="checkbox" name="orientation", value="rot" {orientation}>Rotate<br>
    Wat example should be run?<br>
    {radiostr}
    Text:<br>
    <input type="text" name="text" value="{text}">
    <input type="submit" value="Submit">
        </form>""".format(
            errstr=errstr,
            brightness=brightnessstr,
            text=text,
            update=updatestr,
            orientation=["", "checked"][dorotate],
            radiostr=radiostr
        ), "UTF-8"))

    def do_HEAD(self):
        self._set_headers()
        
def run(server_class=HTTPServer, handler_class=MyHandler, port=80):
    server_address = ('', port)
    try:
        httpd = server_class(server_address, handler_class)
        print ('Starting httpd...')
        httpd.serve_forever()
    except socket.error as e:
        print("Failed to start the server: "+str(e))
        import os
        if (port < 1024) and (os.getuid()!=0):
            print("To start a server on ports below 1024 (like the usual 80 webserver port), you need to be root. So start using sudo.")
    finally:
        scroll_process.terminate()
        
if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        try:
            port=int(argv[1])
        except ValueError:
            print("Usage: webserv.py [portnr], with portnr the port to listen on")
            sys.exit()
    else:
        port=80
    start_scroll_thread()
    run(server_class=HTTPServerV6, port=port)

