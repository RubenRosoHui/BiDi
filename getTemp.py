#!/usr/bin/python

import smbus
import signal
import warnings
from gpiozero import LED
from time import sleep
from sys import exit
from math import log

# preset temperature to warn for user
warningTemp = 20
# Setup, initiate LED
led = LED(21)
# Define some device parameters
I2C_ADDR = 0x48  # I2C device address
# initalize serial bus
bus = smbus.SMBus(1)

def getTemp():
    # prepare bus for reading
    bus.write_byte(I2C_ADDR, 0x40)  # read from AIN0(0x40)
    # dummy read to clear previous reading
    bus.read_byte(I2C_ADDR)
    # read thermistor
    therm_raw = bus.read_byte(I2C_ADDR)
    # calculate the voltage
    volt = therm_raw * 3.3 /225.0
    # calculate the resistance value of thermistor
    Rt = 10.0 * volt / (3.3 - volt)
    # calculate temperature(Kelvin)
    tempK = 1/(1/(273.15 + 25) + log(Rt/10) / 3950)
    # calculate temperature(Celsius)
    tempC = tempK - 273.15
    return '{:2.1f}'.format(tempC) # decimal 1 places

def saveFile(currentTemp):
    # open file as DB
    file = open("temperatureDB.txt", "a+") # append mode
    # write temperature value to the file
    # if value is greater than warning temperature
    if float(currentTemp) >= warningTemp :
        # write the value and add * after the value as a warning state
        file.write("\n%s*" % (currentTemp))
    else :
        file.write("\n%s" %(currentTemp)) # write the value in new line
    # close the file
    file.close()

try:
    while(True):
        # get temperature value
        currentTemp = getTemp()
        saveFile(currentTemp)
        # blink LED when temperature is greater than warning temp.
        if float(currentTemp) >= warningTemp :
            led.on()
            sleep(1)
            led.off()
            sleep(1)
            led.on()
            sleep(1)
            led.off()
        else :
            led.off()
            sleep(3)
        # keep total sleep time to 3 seconds to get data every 3 seconds

except KeyboardInterrupt:
    led.off()
    exit(1)