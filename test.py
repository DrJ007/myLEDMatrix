#
# Drive a 8x8 LED matrix using a MAX7219
#
# frederic.boulanger@centralesupelec.fr
# 2015-05-28
# copyright CentraleSupelec
#
import myLED
import pyb


# An image as a list of integer lines
smiley = (
    0B00111100,
    0B01000010,
    0B10100101,
    0B10000001,
    0B10100101,
    0B10011001,
    0B01000010,
    0B00111100
)
 
# An image as a matrix of objects (True = on, None/False = off)
smiley2 = (
    (None, None, True, True, True, True, None, None),
    (None, True, None, None, None, None, True, None),
    (True, None, True, None, None, True, None, True),
    (True, None, None, None, None, None, None, True),
    (True, None, True, None, None, True, None, True),
    (True, None, None, True, True, None, None, True),
    (None, True, None, None, None, None, True, None),
    (None, None, True, True, True, True, None, None)
)
 
# An image as a list of strings (space = off, others = on)
frowney = (
    '  ....  ',
    ' .    . ',
    '. .  . .',
    '.      .',
    '.  ..  .',
    '. .  . .',
    ' .    . ',
    '  ....  '
)


myMatrix = myLED.matrix() 
 
for i in range(8):
    myMatrix.writeColumn(i, 0xFF)
    pyb.delay(500)
    myMatrix.writeColumn(i, 0x00)
 
for y in range(8):
    for x in range(8):
        myMatrix.setPixel(x, y, True)
    myMatrix.updateDisplay()
    pyb.delay(500)
    for x in range(8):
        myMatrix.setPixel(x, y, False)
 
while True:
    myMatrix.showImage(smiley)
    pyb.delay(1000)
    myMatrix.showImage(frowney)
    pyb.delay(1000)
    myMatrix.showImage(smiley2)
