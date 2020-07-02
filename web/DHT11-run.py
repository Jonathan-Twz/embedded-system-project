import sqlite3
import json
from flask import Flask, render_template , request, Response
import numpy as np
# import RPi.GPIO as GPIOf

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    result = [3,2]
    templateData={
        'i':str(result[0]),
        'j':str(result[1]),
        'temperature':'555'
    }

    return render_template('DHT11-web.html',**templateData)

@app.route('/getData',methods=['GET','POST'])
def getData():
    conn = sqlite3.connect('./sensor.db')
    c = conn.cursor()
    # data = [round(np.random.rand()*100), round(np.random.rand()*100)]
    c.execute("select * from sensordata")
    data = c.fetchall()[-1]
    print(data)
    return Response(json.dumps(data), mimetype='application/json')

if __name__=='__main__':
    app.run(host='localhost', port=5000, debug=True)
