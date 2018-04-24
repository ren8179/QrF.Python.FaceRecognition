# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for,send_file,send_from_directory,render_template
from werkzeug import secure_filename
import dlib
import cv2
import os
from io import BytesIO

CURRENT_PATH = os.getcwd()  # 获取当前路径
UPLOAD_FOLDER = CURRENT_PATH + '\\uploadimgs'
NEWPATH=CURRENT_PATH + "\\img_dlib"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#人脸分类器
detector = dlib.get_frontal_face_detector()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath=os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            img = cv2.imread(filepath)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            dets = detector(gray, 1)
            imgs = []
            for index, face in enumerate(dets):
                left = face.left()
                top = face.top()
                right = face.right()
                bottom = face.bottom()
                crop_img = img[top:bottom, left:right]
                if index==0:
                    newimgpath=filename
                else:
                    newimgpath=str(index+1)+filename
                cv2.imwrite(NEWPATH+"/"+newimgpath, crop_img) # 框出人脸
                imgs.append(newimgpath)
            #return redirect(url_for('uploaded_file', filename=filename))
            return render_template('list.html', imgs=imgs)
    return '''
    <!doctype html>
    <title>上传照片</title>
    <h1>请上传一张包含人像的照片</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=点击上传>
    </form>
    '''
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(NEWPATH, filename)

@app.route('/fr/<imgName>')
def api_fr(imgName):
    # opencv 读取图片，并显示
    img = cv2.imread(UPLOAD_FOLDER+"/"+imgName)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dets = detector(gray, 1)
    result=""
    for index, face in enumerate(dets):
            left = face.left()
            top = face.top()
            right = face.right()
            bottom = face.bottom()
            crop_img = img[top:bottom, left:right]
            if index==0:
                newimgpath=NEWPATH+"/"+imgName
                result+=newimgpath
            else:
                newimgpath=NEWPATH+"/"+str(index+1)+imgName
                result += ";"+newimgpath
            cv2.imwrite(newimgpath, crop_img) # 框出人脸
    return result

@app.route('/get/<imgName>')
def api_get(imgName):
    return _serve_pil_image(NEWPATH+"/"+imgName)

def _serve_pil_image(pil_img):
    img_io = BytesIO()
    img = cv2.imread(pil_img)
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png', cache_timeout=0)

if __name__ == '__main__':
    #app.run('172.16.40.235',81)
    app.run('127.0.0.1',81)