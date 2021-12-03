import time

from PIL import Image
from flask import Flask
from flask import request
from flask import send_file

from climate_model import climate_model


app = Flask(__name__)
@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    print ("hello")
    return "hi"

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/generatedClimatePhoto', methods=['GET'])
def generatedClimatePhoto():
    return send_file("finalimage.jpg", mimetype='image/jpeg')

@app.route('/submitPhoto', methods=['GET', 'POST'])
def submitPhoto():
    try:
        print(request.form.get('myjsonkey'))
        # print(request.args.get('file'))
        # print(request.form.get('file'))
        # print("form:", request.form.keys())
        # print("args:", request.args.keys())
        # print("files:", request.files.keys())
        
        # request.files.get(fle)
        # fle = request.files.values()[0]
        for fle in request.files.keys():
            # print(request.files.get(fle).save("content_length.JPG"))

            iiimg = Image.open(request.files.get(fle).stream)



        # iiimg = Image.open("test_outside.jpg").convert('RGB')
        # .convert('RGB')
        
        cm = climate_model()
        colored_img = cm.loadInitialImage(img_arr=iiimg)
        gen_mask, rgba = cm.getVegetationImage(original_arr=iiimg, colored_img=colored_img)
        cm.inpaintImage(gen_mask,rgba)
        
        return "Ready"#This happens when the image is fully processed

    except Exception as e:
        # raise e
        print("We got the exception: ",e)
        return "BadGeneration"

app.run('127.0.0.1', port = 5000)