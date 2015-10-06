#
# A script to test the display of a text message using myLEDMatrix.
#
# Written for the pyboard and an 8x8 LED matrix with a MAX7219 display driver.
#
import myLEDMatrix
import pyb

myMatrix = myLEDMatrix.matrix()

myMatrix.setIntensity(10)

myMatrix.showText("Hello!")
 
pyb.delay(1000)
myMatrix.clearDisplay()

