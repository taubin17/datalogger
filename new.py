#!/usr/bin/python

import serial

ser = serial.Serial(
        port = '/dev/ttyAMA0',
        baudrate = 19200,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout = None
        )

print(ser.name)
ser.write('Start\n')
x = ser.readline()

x = x.replace(' |', '')
print (x.decode('utf-8'))
