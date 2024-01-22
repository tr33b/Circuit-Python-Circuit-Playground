# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Blink example for boards with ONLY a NeoPixel LED (e.g. without a built-in red LED).
Includes QT Py and various Trinkeys.
Requires two libraries from the Adafruit CircuitPython Library Bundle.
Download the bundle from circuitpython.org/libraries and copy the
following files to your CIRCUITPY/lib folder:
* neopixel.mpy
* adafruit_pixelbuf.mpy
Once the libraries are copied, save this file as code.py to your CIRCUITPY
drive to run it.
"""
import time
import board
import neopixel

# Calls the circuit Python neopixel library, specifies the default board 
# pins for the Neopixels, and the number of neopixels to access.  Returns a 
# list 'pixels' of indexable neopixles
pixels = neopixel.NeoPixel(board.NEOPIXEL, 9)

while True:
    # indexes the first element of the 'pixels' list and points to the 
    # first (and only) Neopixel in the 'pixels' list
    pixels[0]=(255, 0, 0)
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5)
    pixels[1]=(0,255, 0)
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5)
    pixels[2]=(0, 0, 255)
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5)
    pixels[3]=(0,255, 0)
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5)
    pixels[4]=(255, 0, 0)
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5)
    pixels[5]=(0,255, 0)
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5)
    pixels[6]=(0, 0, 255)
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5)
    pixels[7]=(10,20, 0)
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5)
    pixels[8]=(0, 10, 20)
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5)
