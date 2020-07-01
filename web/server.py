#import pymysql
# import urllib, urllib2s
import json
import sqlite3 as sql
import datetime
import time
import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=2)
now = datetime.datetime.now
conn = sql.connect('sensor.db')
c = conn.cursor()
c.execute("delete from sensordata")
print('serial to sql server started')
if __name__ == "__main__":
    while True:
        try:
            ser.write(b"GET TH")
            response = str(ser.readline().decode())
            if response.startswith('data'):
                serialData = response[4:-2]
                temperature = int(serialData[:2])
                humidity = int(serialData[2:4])
                timenow=str(now())[:-4]
                #print(humidity)
                data = {
                    'time': timenow,
                    'temperature': temperature,
                    'humidity': humidity,
                }
                c.execute("insert into sensordata (time, temperature, humidity) values('%s','%f','%f')"%(timenow, temperature, humidity))
                conn.commit()
        except KeyboardInterrupt:
            ser.close()
            conn.close()
    
# print('commit done')
# c.execute("select * from sensordata")
# data = c.fetchall()
# for row in data:
#     print(row)
# conn.close()
