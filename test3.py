#
# A script to test the display of 8x8 bitmap images using myLEDMatrix.
#
# Uses the space invaders bitmaps from the Adafruit tutorial
# "Trinket/Gemma Space Invader Pendant".
# https://learn.adafruit.com/trinket-slash-gemma-space-invader-pendant/overview
#
# Written for the pyboard and an 8x8 LED matrix with a MAX7219 display driver.
#
import myLEDMatrix
import pyb


alien1f1 = (
    0B00011000, ## This is the first frame for alien #1
    0B00111100, ## If you squint you can kind of see the
    0B01111110, ## image in the 0's and 1's.
    0B11011011,
    0B11111111,
    0B00100100,
    0B01011010,
    0B10100101)

alien1f2 = (
    0B00011000, ## This is the second frame for alien #1
    0B00111100,
    0B01111110,
    0B11011011,
    0B11111111,
    0B00100100,
    0B01011010,
    0B01000010)

alien2f1 = (
  0B00000000, ## First frame for alien #2
  0B00111100,
  0B01111110,
  0B11011011,
  0B11011011,
  0B01111110,
  0B00100100,
  0B11000011)
 
alien2f2 = (
  0B00111100, ## Second frame for alien #2
  0B01111110,
  0B11011011,
  0B11011011,
  0B01111110,
  0B00100100,
  0B00100100,
  0B00100100)

alien3f1 = (
  0B00100100, ## First frame for alien #3
  0B00100100,
  0B01111110,
  0B11011011,
  0B11111111,
  0B11111111,
  0B10100101,
  0B00100100)
 
alien3f2 = (
  0B00100100, ## Second frame for alien #3
  0B10100101,
  0B11111111,
  0B11011011,
  0B11111111,
  0B01111110,
  0B00100100,
  0B01000010)

alien4f1 = (
  0B00111100, ## First frame for alien #4
  0B01111110,
  0B00110011,
  0B01111110,
  0B00111100,
  0B00000000,
  0B00001000,
  0B00000000)
 
alien4f2 = (
  0B00111100, ## Second frame for alien #4
  0B01111110,
  0B10011001,
  0B01111110,
  0B00111100,
  0B00000000,
  0B00001000,
  0B00001000)
 
alien4f3 = (
  0B00111100, ## Third frame for alien #4 (NOT a repeat of frame 1)
  0B01111110,
  0B11001100,
  0B01111110,
  0B00111100,
  0B00000000,
  0B00000000,
  0B00001000)
 
alien4f4=(
  0B00111100, ## Fourth frame for alien #4 (NOT a repeat of frame 2)
  0B01111110,
  0B01100110,
  0B01111110,
  0B00111100,
  0B00000000,
  0B00000000,
  0B00000000)
 

myMatrix = myLEDMatrix.matrix()

myMatrix.setIntensity(10)

while True: 
    for i in range(2):
        myMatrix.showImage(alien1f1)
        pyb.delay(250)
        myMatrix.showImage(alien1f2)
        pyb.delay(250)

    for i in range(2):
        myMatrix.showImage(alien2f1)
        pyb.delay(250)
        myMatrix.showImage(alien2f2)
        pyb.delay(250)

    for i in range(2):
        myMatrix.showImage(alien3f1)
        pyb.delay(250)
        myMatrix.showImage(alien3f2)
        pyb.delay(250)

    for i in range(2):
        myMatrix.showImage(alien4f1)
        pyb.delay(120)
        myMatrix.showImage(alien4f2)
        pyb.delay(120)
        myMatrix.showImage(alien4f3)
        pyb.delay(120)
        myMatrix.showImage(alien4f4)
        pyb.delay(120)



