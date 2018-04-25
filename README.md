# QrF.Python.FaceRecognition
Python 人脸识别技术 

初始灵感及代码来自于 vipstone 大神的 [faceai](https://github.com/vipstone/faceai) 项目

### FaceRecognition_dir_OpenCV.py

使用OpenCV来识别人脸
遍历 img_upload 文件夹下的所有图片，识别每张图片的人脸，并保存到 img_cv 文件夹
详细说明请参考 [https://github.com/vipstone/faceai/blob/master/doc/jiance.md](https://github.com/vipstone/faceai/blob/master/doc/jiance.md)

### FaceRecognition_dir_dlib.py

使用dlib来识别人脸
遍历 img_upload 文件夹下的所有图片，识别每张图片的人脸，并保存到 img_dlib 文件夹
详细说明请参考 [https://github.com/vipstone/faceai/blob/master/doc/jiance-dlib.md](https://github.com/vipstone/faceai/blob/master/doc/jiance-dlib.md)

### app.py

使用Flask框架及dlib 来支持通过Web的方式实现 上传照片中人脸识别功能

app.run('127.0.0.1',81) 这里配置服务器的访问IP及端口

### imghandler.py

改变图片分辨率

### 使用以及借鉴的开源项目清单


> [faceai](https://github.com/vipstone/faceai) 一款优秀的人脸检测、人脸识别、视频识别、文字识别等智能AI项目。

> [flask](https://github.com/pallets/flask) 一个 Python 实现的 Web 开发微框架

> [opencv](https://github.com/opencv/opencv) 一个跨平台的计算机视觉处理库
