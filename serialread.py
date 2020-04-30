#!/usr/bin/python

import time, datetime
from datetime import date
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


#Open the file here to write data out
fd = open('datalogger.dat', 'w')
    
#Send a "character" to serial to initialize data. Also track the time we recieve data back
print("Start : %s" % time.ctime())
ser.write('Start\n')
time.sleep(0.100)
ser.flushInput()
x = ser.readline()
ser.flushOutput()

#Parse the data to be split by spaces, rather than by pipes.
x = x.replace(' |', '')

#Split data by each sensor result
parsed = x.split()
    
#Grab the sensor results we want
data = [parsed[0], parsed[7], parsed[6], parsed[4], parsed[1], parsed[2], parsed[3], parsed[5]]
    
#Confirm the data is correct
print data

#Write to data file the date and time
grab_time = time.ctime()
parse_time = grab_time.split()
my_time = parse_time[3]
string_date = str(date.today())

fd.write(string_date),
fd.write(" "),
fd.write(my_time),

#Write all sensor values seperated by spaces to data file
fd.write(" "),
fd.write(data[0]),
fd.write(" "),
fd.write(data[1]),
fd.write(" "),
fd.write(data[2]),
fd.write(" ")
fd.write(data[3]),
fd.write(" "),
fd.write(data[4]),
fd.write(" "),
fd.write(data[5]),
fd.write(" "),
fd.write(data[6]),
fd.write(" "),
fd.write(data[7]),
fd.write(" "),

    
#Write a new line after each data and date/time entry
fd.write("\n")
fd.close() 
exec(open("SQLite.py").read())

#Cleanup file descriptors
fd.close()
#Leave
exit
