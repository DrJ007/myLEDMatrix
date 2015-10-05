#
# Drive a 8x8 LED matrix using a MAX7219
#
# frederic.boulanger@centralesupelec.fr
# 2015-05-28
# copyright CentraleSupelec
#
import pyb

class constants(object):     
    # Register for controlling the operation mode
    ShutdownRegister = 0x0C
    shutdownMode = 0B00000000;      # display off
    normalOperation = 0B00000001    # display on
     
    # Register for controlling the number of digits to drive
    ScanLimitRegister = 0x0B
     
    # Register for controlling the test mode
    DisplayTestRegister = 0x0F
    noTest = 0B00000000  # normal operation
    doTest = 0B00000001  # test (light up all segments)
     
    # Register for controlling the decoding of digit values
    DecodeRegister = 0x09
    noDecode = 0x00  # No decoding, bits drive individual LEDs
    codeB = 0xFF     # Decoding according to B code (not useful with an LED matrix)
     
    # Register for controlling the intensity of the segments 0=minimum, 15=maximum)
    IntensityRegister = 0x0A
 
    # Register holding the value for column 0 (leftmost) to 7 (rightmost)
    columnRegister = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08]


class matrix(object):
    def __init__(self):
        # Bitmap for holding the LED state
        self.bitmap = bytearray(8)
        
        data = pyb.Pin.board.Y1;    # MAX7219 serial data in pin
        load = pyb.Pin.board.Y2;    # Register load pin
        clk = pyb.Pin.board.Y3;     # Serial shift clock pin

        # Initialize the pins of the pyboard in output push-pull mode
        self.dataPin = pyb.Pin(data, pyb.Pin.OUT_PP)
        self.loadPin = pyb.Pin(load, pyb.Pin.OUT_PP)
        self.clkPin = pyb.Pin(clk, pyb.Pin.OUT_PP)
         
        # Set all pins to low
        self.dataPin.low()
        self.loadPin.low()
        self.clkPin.low()
         
        # Configure the MAX7219 to use 8 rows (0 to 7)
        self.serialWrite(constants.ScanLimitRegister,7)
        # use rows 0 to 7
         
        # Set the display intensity to half of the maximum
        self.setIntensity(25)
        # Put the MAX7219 in normal operation (it is off when starting)
        self.serialWrite(constants.ShutdownRegister, constants.normalOperation)
        # Put the MAX7219 in test mode (display all segments of all digits)
        self.serialWrite(constants.DisplayTestRegister, constants.doTest)
        # Wait for 2s
        pyb.delay(2000)
        # Get out of test mode
        self.serialWrite(constants.DisplayTestRegister, constants.noTest)
        self.clearDisplay()
        # Wait for 1s
        pyb.delay(1000)
         
        self.serialWrite(constants.DecodeRegister, constants.noDecode)

        
        
    # Shift a byte into the serial register of the MAX7219, MSB first
    def serialShiftByte(self, data):
        # Put the shift clock and load signal to low in order to make a rising edge later
        self.loadPin.low()
        self.clkPin.low()
        # Shift the 8 bits of data
        for i in range(8):
            value = ((data << i) & 0B10000000) != 0
            self.dataPin.value(value)
            self.clkPin.high()
            self.clkPin.low()
     
    # Load the shifted data into the MAX7219 register
    def loadRegisterFromShift(self):
        # Make a pulse on the load clock to load the shifted data into the register
        self.loadPin.high()
        self.loadPin.low()
     
    # Write some data to an address in the MAX7219.
    # The address+data are shifted MSB first as a 16 bit word into the MAX7219, then loaded.
    def serialWrite(self,address, data):
        self.serialShiftByte(address)
        self.serialShiftByte(data)    
        self.loadRegisterFromShift()
     
    # Set the intensity of the segments in percents of the max intensity
    def setIntensity(self,percent):
        value = int((percent * 15)/100)
        self.serialWrite(constants.IntensityRegister, value)
     
    # Write a value to a column of the LED matrix (the MAX7219 should be in no decode mode)
    def writeColumn(self,colNum, value):
        self.serialWrite(constants.columnRegister[colNum], value)
     
    # Clear the bitmap
    def clearBitmap(self):
        for i in range(8):
            self.bitmap[i] = 0
     
    # Update the display with the bitmap contents
    def updateDisplay(self):
        for i in range(8):
            self.writeColumn(i, self.bitmap[i])
     
    # Turn all LEDs off
    def clearDisplay(self):
        self.clearBitmap()
        self.updateDisplay()
     
    # Set LED on column x, line y (0 = top) on or off
    def setPixel(self, x, y, on):
        if on:
            self.bitmap[x] |= 2**y
        else:
            self.bitmap[x] &= (0xFF - 2**y)
     
    def showImage(self, image):
        if not isinstance(image, (list, tuple)):
            raise RuntimeError("Image is not a list")
        if len(image) != 8:
            raise RuntimeError("Image does not have 8 components")
        if isinstance(image[0], int):
            for i in range(8):
                value = image[i]
                for j in range(8):
                    self.setPixel(j, i, value & 2**(7 - j))
        elif isinstance(image[0], str):
            for i in range(8):
                if len(image[i]) != 8:
                    raise RuntimeError("String in image does not have 8 character")
                for j in range(8):
                    self.setPixel(j, i, image[i][j] != ' ')
        elif isinstance(image[0], (tuple, list)):
            for i in range(8):
                if len(image[i]) != 8:
                    raise RuntimeError("List in image does not have 8 items")
                for j in range(8):
                    self.setPixel(j, i, image[i][j])
        else:
            raise RuntimeError("Could not interpret image")
        self.updateDisplay()
 
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


myMatrix = matrix() 
 
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
