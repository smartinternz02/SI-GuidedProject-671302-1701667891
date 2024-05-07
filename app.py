import os
from flask import Flask, render_template, request
from werkzeug.utils import  send_from_directory
from ultralytics import YOLO
from flask import Flask

app = Flask(__name__)

model = YOLO('yolov8l.pt')

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/", methods=["GET", "POST"])
def predict_img():
    if request.method == "POST":
        if 'file' in request.files:
            f = request.files['file']
            basepath = os.path.dirname(__file__)
            filepath = os.path.join(basepath,'uploads', f.filename)
            f.save(filepath)
            global imgpath
            predict_img.imapath = f.filename
            file_extension = f.filename.rsplit ('.', 1)[1].lower()
            if file_extension == 'jpg':
                source=filepath
                detections = model.predict(source, save=True,show=True,imgsz=320, conf=0.5)
    return display(f.filename)

@app.route('/<path:filename>')
def display(filename) :
    folder_path = 'runs/detect'
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    latest_subfolder = max(subfolders, key=lambda x:os.path.getctime(os.path.join(folder_path, x)))
    directory = folder_path+'/'+latest_subfolder
    files = os.listdir(directory)
    index = files.index(filename)
    latest_file = files[index]
    filename = os.path.join(folder_path, latest_subfolder, latest_file)
    file_extension = filename.rsplit('.', 1)[1].lower()
    environ = request.environ
    if file_extension == 'jpg':
        return send_from_directory(directory, latest_file,environ) 
    else: 
        return "Invalid file format"

if __name__ == "__main__":
    print("Server Started")
    app.run()