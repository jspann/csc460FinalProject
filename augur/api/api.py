import time
from flask import Flask

app = Flask(__name__)
@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    print ("hello")
    return "hi"

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

app.run('127.0.0.1', port = 5000)