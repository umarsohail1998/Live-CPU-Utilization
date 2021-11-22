import json
from time import time
from random import random
from flask import Flask, render_template, make_response
from psutil import *


app = Flask(__name__, 
            static_url_path='/static',
            static_folder="/static")
lt = []

@app.route('/')
def hello_world():
    return render_template('index.html', data='test')

@app.route('/live-data')
def live_data():
    data = [time() * 1000, cpu_percent(0.1, percpu=True)]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
