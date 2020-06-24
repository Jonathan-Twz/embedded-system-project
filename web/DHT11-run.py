from DHT11 import fun
# import json
from flask import Flask, render_template , request, send_file
# import RPi.GPIO as GPIOf

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    aa = 0
    result = fun(aa)
    
    return render_template('DHT11-web.html',i = str(result[0]), j= str(result[1]))

if __name__=='__main__':
    app.run(host='localhost', port=5000, debug=True)
