#!/usr/bin/python

import sqlite3
import time

#Loop to grab the newest line. We will use SQL commands to remove the old entries!
fd = open('datalogger.dat', 'r')

data = fd.readline()
parsed = data.split()


#Set each field of the table to its respective result from split()
my_date = parsed[0]
my_time = parsed[1]
high_res_temperature = parsed[2]
humidity = ((float(parsed[3])) / 1000) #Convert from millipercent
pressure = ((float(parsed[4])) / 10000000)#Convert from hundreds of micro bar to bar
light = parsed[5]
IR_intensity = parsed[6]
Full_Spectrum = parsed[7]
Visible_Light = parsed[8]
low_res_temperature = ((float(parsed[9])) / 100)

#Confirm the current data has successfully entered SQL script
print(parsed)

connection = sqlite3.connect('SensorData.db')
#Create cursor to control database
cursor = connection.cursor()
#Create our table if it doesn't exist
cursor.execute('CREATE TABLE IF NOT EXISTS date_time (date date, time time, high_res_temperature FLOAT, humidity FLOAT, pressure FLOAT, light INT, IR_intensity INT, Full_Spectrum INT, Visible_Light INT, low_res_temperature FLOAT)')
#Take the data value held in the file and upload it, separating each element of time, data, and the date
cursor.execute('INSERT INTO date_time VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (my_date, my_time, high_res_temperature, humidity, pressure, light, IR_intensity, Full_Spectrum, Visible_Light, low_res_temperature))
#IF our entries tally more than 1400 at any time, starting at the bottom of the stack (SQL IS LIFO), remove beginning elements
cursor.execute('DELETE FROM date_time WHERE ROWID IN (SELECT ROWID FROM date_time ORDER BY ROWID DESC LIMIT -1 OFFSET 1439)')
connection.commit()
#connection.close()
