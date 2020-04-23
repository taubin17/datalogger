#!/usr/bin/python

import sqlite3

#Loop to grab the newest line. We will use SQL commands to remove the old entries!
fd = open('datalogger.dat', 'r')

data = fd.readline()
parsed = data.split()

print(parsed)

connection = sqlite3.connect('SensorData.db')
cursor = connection.cursor()
#cursor.execute('DELETE FROM date_time WHERE ROWID IN (SELECT ROWID FROM date_time ORDER BY ROWID DESC LIMIT -1 OFFSET 1400)')
cursor.execute('CREATE TABLE IF NOT EXISTS date_time (day_of_week TEXT, month TEXT, day TEXT, time TEXT, year TEXT, temperature FLOAT, humidity FLOAT, pressure FLOAT, light INT)')
cursor.execute('INSERT INTO date_time VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', (parsed[0], parsed[1], parsed[2], parsed[3], parsed[4], parsed[5], parsed[6], parsed[7], parsed[8]))
connection.commit()
