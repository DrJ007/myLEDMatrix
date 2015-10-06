MAX7219 Driver
==============

A MAX7219 driver for an 8x8 LED matrix display in microPython for the pyboard.

Tested using a LinkSprite LED Matrix Kit V1.

Based on MAX7219.py by frederic.boulanger@centralesupelec.fr at
http://wwwdi.supelec.fr/fb/Archi2015/PyBoardMAX7219-8x8.

Modified to use pyb.SPI and classes.

Uses CP437_FONT from Richard Hull's MAX7219 driver.
https://github.com/rm-hull/max7219

License
-------
The MIT License (MIT)

Copyright (c) 2015 Jeanne Young

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.