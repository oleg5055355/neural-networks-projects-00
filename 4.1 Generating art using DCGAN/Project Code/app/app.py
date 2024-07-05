from flask import Flask, render_template, request
import numpy as np
import os
from model import generate
import cv2
import matplotlib.pyplot as plt
#import pandas as pd

app = Flask(__name__)


UPLOAD_FOLDER = '/Users/adityavs14/Documents/Internship/Pianalytix/Month_2/DCGAN/app/static'
ALLOWED_EXTENSIONS = set(['png','jpg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


img_rows, img_cols, channels = 128,128,3


@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        path = os.path.join(app.config['UPLOAD_FOLDER'], 'input.png')
        plt.switch_backend('Agg')
        image = generate()
        image = image.reshape((img_rows, img_cols, channels)).astype('uint8')
        image = cv2.resize(image, (512,512), interpolation = cv2.INTER_AREA)
        plt.imshow(image)
        plt.axis('off')
        plt.imsave(path,image)
    return render_template('index.html') 





if __name__ == "__main__":
    app.run(debug=True)