#import pymysql
import sqlite3 as sql
import datetime
import time

#conn = pymysql.connect(host='localhost',port=3306,user='root',
 #           password='jonathan',db='sensor',charset='utf8')

conn = sql.connect('sensor.db')
c = conn.cursor()
now = datetime.datetime.now

c.execute("delete from sensordata")

for i in range(30):
    timenow=str(now())[:-4]
    c.execute("insert into sensordata (time, temperature, humidity) values('%s','%f','%f')"%(timenow,i, i*2))
    conn.commit()
    time.sleep(0.1) #sleep 1 sec after commit
    
print('commit done')
c.execute("select * from sensordata")
data = c.fetchall()
for row in data:
    print(row)
conn.close()
#print(data)