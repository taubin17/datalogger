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


#Grab data forever
while True:
    
    #Open the file here to write data out
    fd = open('datalogger.dat', 'w')
    

    #Send a "character" to serial to initialize data. Also track the time we recieve data back
    print("Start : %s" % time.ctime())
    ser.write('Start\n')
    x = ser.readline()
    #Parse the data to be split by spaces, rather than by pipes.
    
    x = x.replace(' |', '')
    #Split data by each sensor result
    parsed = x.split()
    
    #Grab the sensor results we want
    data = [parsed[0], parsed[7], parsed[6], parsed[4]]
    
    #Confirm the data is correct
    print data

    #Write to data file the date and time
    fd.write(time.ctime()),
    
    #Write all sensor values seperated by spaces to data file
    fd.write(" "),
    fd.write(data[0]),
    fd.write(" "),
    fd.write(data[1]),
    fd.write(" "),
    fd.write(data[2]),
    fd.write(" ")
    fd.write(data[3]),
    fd.write(" ")
    
    #Write a new line after each data and date/time entry
    fd.write("\n")
    fd.close() 
    exec(open("SQLite.py").read())
    #Wait a minute to repeat the loop
    time.sleep(60)
    print("End : %s" % time.ctime())
    print
    print
    
#Cleanup file descriptors
fd.close()
#Leave
exit
