.. role:: python(code)
   :language: python

Welcome
-------

Welcome to the Scroll pHAT documentation. This page will guide you through the methods
available in the Scroll pHAT python library.

The Scroll pHAT provides a matrix of 55 white LED pixels that is ideal for writing messages, showing graphs, and drawing pictures. Use it to output your IP address, show CPU usage, or just play pong!

* Learn more about Scroll pHAT: https://shop.pimoroni.com/products/scroll-phat
* Contribute examples & fixes: https://github.com/pimoroni/scroll-phat

At A Glance
-----------

.. automoduleoutline:: scrollphat
   :members:

.. toctree::
   :titlesonly:
   :maxdepth: 0

Set A Single Pixel In Buffer
----------------------------

Scroll pHAT uses white LEDs which can be either on or off.

When you set a pixel it will not immediately display on Scroll pHAT, you must call :python:`scrollphat.update()`.

.. automodule:: scrollphat
   :noindex:
   :members: set_pixel

Set All Pixels In Buffer
------------------------

.. automodule:: scrollphat
   :noindex:
   :members: set_pixels

Write A Text String
-------------------

.. automodule:: scrollphat
   :noindex:
   :members: write_string

Display Buffer
--------------

All of your changes to Scroll pHAT are stored in a Python buffer. To display them
on Scroll pHAT you must call :python:`scrollphat.update()`.

.. automodule:: scrollphat
   :noindex:
   :members: update

Clear Buffer
------------

.. automodule:: scrollphat
   :noindex:
   :members: clear_buffer

Clear Buffer And Display
------------------------

.. automodule:: scrollphat
   :noindex:
   :members: clear

Set The Brightness
------------------

.. automodule:: scrollphat
   :noindex:
   :members: set_brightness

Scroll The Buffer
-----------------

.. automodule:: scrollphat
   :noindex:
   :members: scroll

Scroll To A Position
--------------------

.. automodule:: scrollphat
   :noindex:
   :members: scroll_to

Rotate The Display
------------------

.. automodule:: scrollphat
   :noindex:
   :members: set_rotate

Constants
---------

:python:`ROTATE_OFF = False`

:python:`ROTATE_180 = True`