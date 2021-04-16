#!/usr/bin/python

import smbus
import signal
import warnings
from gpiozero import LED
from time import sleep
from sys import exit
from math import log
import threading


# preset temperature to warn to user
warningdB = 10
# Setup, initiate LED
led = LED(21)
# Define some device parameters
I2C_ADDR = 0x48  # I2C device address
# initalize serial bus
bus = smbus.SMBus(1)

def getSound():
    # prepare bus for reading
    bus.write_byte(I2C_ADDR, 0x41)  # read from AIN1(0x41)
    # dummy read to clear previous reading
    bus.read_byte(I2C_ADDR)
    # read thermistor
    sound_raw = bus.read_byte(I2C_ADDR)
    return sound_raw

def getRef():
    soundRef = 0
    getSound()
    for i in range(10):
        sleep(0.1)
        soundRef+=getSound()

    soundRef/=10
    return soundRef

def saveFile(currentSound):
    # open file as DB
    file = open("soundDB.txt", "a+") # append mode
    # write sound value to the file
    # if value is greater than warning value, then
    if currentSound >= warningdB:
        file.write("\n%d*" % (currentSound)) # add * after the value
    else :
        file.write("\n%d" %(currentSound)) # write the value in new line
    # close the file
    file.close()


soundRef = float(getRef())

while (True):
    sound_raw = float(getSound())
    temp = sound_raw / soundRef
    db = 20 * log(temp, 10)
    print(db)
    saveFile(db)
    sleep(0.3)