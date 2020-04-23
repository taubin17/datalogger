#!/usr/bin/python

import sqlite3
import time

#Loop to grab the newest line. We will use SQL commands to remove the old entries!
fd = open('datalogger.dat', 'r')

data = fd.readline()
parsed = data.split()


#Set each field of the table to its respective result from split()
day_of_week = parsed[0]
month = parsed[1]
day = parsed[2]
time_now = parsed[3]
year = parsed[4]
temperature = parsed[5]
humidity = parsed[6]
pressure = parsed[7]
light = parsed[8]

#Confirm the current data has successfully entered SQL script
print(parsed)

connection = sqlite3.connect('SensorData.db')
#Create cursor to control database
cursor = connection.cursor()
#Create our table if it doesn't exist
cursor.execute('CREATE TABLE IF NOT EXISTS date_time (day_of_week TEXT, month TEXT, day TEXT, time TEXT, year TEXT, temperature FLOAT, humidity FLOAT, pressure FLOAT, light INT)')
#Take the data value held in the file and upload it, separating each element of time, data, and the date
cursor.execute('INSERT INTO date_time VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', (day_of_week, month, day, time_now, year, temperature, humidity, pressure, light))
#IF our entries tally more than 1400 at any time, starting at the bottom of the stack (SQL IS LIFO), remove beginning elements
cursor.execute('DELETE FROM date_time WHERE ROWID IN (SELECT ROWID FROM date_time ORDER BY ROWID DESC LIMIT -1 OFFSET 1439)')
connection.commit()
#connection.close()
