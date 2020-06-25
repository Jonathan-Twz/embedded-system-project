import sqlite3
import json
from flask import Flask, render_template , request, send_file
# import RPi.GPIO as GPIOf

conn = sqlite3.connect('./sensor.db')
c = conn.cursor()

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    result = [4,2]

    templateData={
        'i':str(result[0]),
        'j':str(result[1])
    }

    # if request.method == 'GET':
    #     templateData = request.json
    #     try:
    #         # cmd = 'select TOP 1 * from sensordata'
    #         cmd = 'select * from sensordata'
    #         c.execute(cmd)
    #         data = c.fetchall()
    #         print(data[-1])
    #     except 
    return render_template('DHT11-web.html',**templateData)

if __name__=='__main__':
    app.run(host='localhost', port=5000, debug=True)
