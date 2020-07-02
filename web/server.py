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
                data = response[5:]
                temperature = int(data[:2])
                humidity = int(data[3:5])
                light = int(data[6:9])
                gas = int(data[10:13])
                rain = int(data[14:18])
                voice = int(data[19])
                track = int(data[21])
                alert_flag = int(data[23])
                timenow=str(now())[:-4]
                
                c.execute("insert into sensordata (time, temperature, humidity, light, gas, rain, voice, track, alter_flag) values('%s','%d','%d','%d','%d','%d','%d','%d','%d')"%(timenow, temperature, humidity, light, gas, rain, voice, track, alert_flag))
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
