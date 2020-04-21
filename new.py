#!/usr/bin/python

import serial
ser = serial.Serial('/dev/ttyACM0')
print(ser.name)
ser.write(b's')
x = ser.read()
