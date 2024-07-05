from flask import Flask, render_template, request
import numpy as np
import os
from model import image_pre,predict
#import seaborn as sns
import matplotlib.pyplot as plt
#import pandas as pd

app = Flask(__name__)


UPLOAD_FOLDER = '/Users/adityavs14/Documents/Internship/Pianalytix/Month_2/Builtup/app/static'
ALLOWED_EXTENSIONS = set(['tif','tiff','png'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER





@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], 'input.tif')
        path2 = os.path.join(app.config['UPLOAD_FOLDER'], 'output.png')
        file1.save(path)
        data,shape= image_pre(path)
        s = predict(data,shape)
        plt.switch_backend('Agg')
        plt.imshow(s)
        plt.imsave(path2,s,cmap='gray')
    return render_template('index.html') 





if __name__ == "__main__":
    app.run(debug=True)