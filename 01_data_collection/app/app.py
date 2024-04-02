import os

import cv2
from flask import Flask, Response, render_template, jsonify, request, make_response, send_file
from cam import Camera
import datetime as dt
import logging
from pathlib import Path
import shutil
import zipfile
from azure.storage.blob import BlockBlobService



app = Flask(__name__)

cam = Camera()

parent_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(parent_path, 'static', 'images')

logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
handler = logging.FileHandler('test.log') # creates handler for the log file
logger.addHandler(handler)

logger.info('ParentPath' + parent_path)

if not os.path.exists(image_path):
    os.mkdir(image_path)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed', methods=['GET'])
def video_feed():
    global cam
    return Response(cam.stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')




@app.route('/zoom', methods=['POST'])
def zoom():
    zoom_value = request.form.get('zoom')
    print(zoom_value)
    cam.zoom(1-float(zoom_value))
    data = {'zoom':zoom_value}
    return  jsonify(data)


@app.route('/capture', methods=['POST'])
def capture():
    score = request.form.get('score')
    path = os.path.join(image_path, str(dt.datetime.now()) +'_'+ score+ '.jpg')
    cam.capture(image_path, score)
    return  jsonify({'data': path})


@app.route('/list_images', methods=['GET'])
def list_images():
    #files = os.listdir(image_path)
    files = [s for s in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, s))]
    files.sort(key=lambda s: os.path.getmtime(os.path.join(image_path, s)), reverse=True)

    files = [os.path.join('/static/images', i) for i in files if i != '.gitignore' and i.endswith('.zip') == False]
    data = {'data':files}
    return jsonify(data)


@app.route('/delete', methods= ['POST'])
def delete():
    file = os.path.basename(request.form.get('img'))
    path = os.path.join(image_path, file)
    os.remove(path)
    return  jsonify({'img': path})

@app.route('/download', methods=['GET'])
def download():
    file_path = os.path.join(parent_path, 'static', 'download.zip')
    zf = zipfile.ZipFile(file_path, "w")
    for dirname, subdirs, files in os.walk(image_path):
        zf.write(dirname)
        for filename in files:
            if filename.endswith('.jpg'):
                zf.write(os.path.join(dirname, filename))
    zf.close()

    return jsonify({})
    
@app.route('/sync', methods=['POST'])
def sync():
    blob_service = BlockBlobService(os.getenv('BLOB_ACCOUNT'), os.getenv('BLOB_KEY'))

    for dirname, subdirs, files in os.walk(image_path):
        for filename in files:
            if filename.endswith('.jpg'):
                blob_service.create_blob_from_path('raw-imgs', filename ,  os.path.join(dirname, filename) )
                os.remove( os.path.join(dirname, filename) )
    return jsonify({})

@app.route('/beta', methods=['POST'])
def beta():
    value = request.form.get('beta')
    cam.beta = float(value)
    data = {'beta':value}
    return  jsonify(data)

@app.route('/alpha', methods=['POST'])
def alpha():
    value = request.form.get('alpha')
    cam.alpha = float(value)
    data = {'alpha':alpha}
    return  jsonify(data)


if __name__ == '__main__':





    app.run(host='0.0.0.0', port=7007, threaded=True)