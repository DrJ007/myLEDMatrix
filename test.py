#
# A script to test the display of 8x8 bitmap images using myLEDMatrix.
#
# Written for the pyboard and an 8x8 LED matrix with a MAX7219 display driver.
#
import myLEDMatrix
import pyb

myMatrix = myLEDMatrix.matrix()

myMatrix.setIntensity(10)

myMatrix.runTest()

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
        
myMatrix.clearDisplay()

