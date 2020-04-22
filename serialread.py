#!/usr/bin/python

import serial
import time

ser = serial.Serial(
        port = '/dev/ttyAMA0',
        baudrate = 19200,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout = None
        )

print(ser.name)

#Open file to write data
fd = open("datalogger.dat", "a");

while True:
    print("Start : %s" % time.ctime())
    ser.write('Start\n')
    x = ser.readline()

    x = x.replace(' |', '')
    print (x.decode('utf-8')),
    fd.write(x.decode('utf-8'))
    time.sleep(60)
    print("End : %s" % time.ctime())
    print
    print
    
fd.close()
exit
