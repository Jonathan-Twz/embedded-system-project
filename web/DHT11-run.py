import sqlite3
import json
from flask import Flask, render_template , request, Response
import numpy as np
# import RPi.GPIO as GPIOf

conn = sqlite3.connect('./sensor.db')
c = conn.cursor()

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    result = [1,2]
    templateData={
        'i':str(result[0]),
        'j':str(result[1]),
        'temperature':'555'
    }

    # if request.method == 'GET':
    #     templateData = request.json
    #     try:
    #         # cmd = 'select TOP 1 * from sensordata'
    #         cmd = 'select * from sensordata'
    #         c.execute(cmd)
    #         data = c.fetchall()
    #         print(data[-1])
    #     except :
    #         pass
    return render_template('DHT11-web.html',**templateData)

@app.route('/getdata',methods=['GET','POST'])
def getData():
    data = [round(np.random.rand()*100), round(np.random.rand()*100)]
    return Response(json.dumps(data), mimetype='application/json')


if __name__=='__main__':
    app.run(host='localhost', port=5000, debug=True)
