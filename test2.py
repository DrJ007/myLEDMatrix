#
# Drive a 8x8 LED matrix using a MAX7219
#
# frederic.boulanger@centralesupelec.fr
# 2015-05-28
# copyright CentraleSupelec
#
import myLED
import pyb

myMatrix = myLED.matrix()

myMatrix.setIntensity(10)

myMatrix.runTest()

myMatrix.showText("Hello!")
 
pyb.delay(1000)
myMatrix.clearDisplay()

