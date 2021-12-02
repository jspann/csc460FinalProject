import time
from flask import Flask
from flask import request


app = Flask(__name__)
@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    print ("hello")
    return "hi"

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/submitPhoto', methods=['GET', 'POST'])
def submitPhoto():
    try:
        print(request.form.get('myjsonkey'))
        # print(request.args.get('file'))
        # print(request.form.get('file'))
        # print("form:", request.form.keys())
        # print("args:", request.args.keys())
        # print("files:", request.files.keys())
        for fle in request.files.keys():
            print(request.files.get(fle).save("content_length.JPG"))

        return "words"
    except Exception as e:
        # raise e
        print("We got the exception: ",e)
        return "Nah"

app.run('127.0.0.1', port = 5000)