from flask import Flask, render_template, request
import numpy as np
import os
from model import image_pre,predict
#import seaborn as sns
#import matplotlib.pyplot as plt
#import pandas as pd

app = Flask(__name__)


UPLOAD_FOLDER = '/Users/adityavs14/Documents/Internship/Pianalytix/Month_2/WeedDetection/app/static'
ALLOWED_EXTENSIONS = set(['tif','tiff'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
output = ['broadleaf', 'grass', 'soil', 'soybean']




@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], 'input.png')
        file1.save(path)
        data,img = image_pre(path)
        s = predict(data)
        img.save(path)
        if s == 0:
            result = output[0] + ' weed'
        elif s == 1 :
            result = output[1] + ' weed'
        elif s == 2 :
            result = output[2] + ' weed'
        else :
            result = output[3] + ' weed'
    return render_template('index.html',result=result) 





if __name__ == "__main__":
    app.run(debug=True)