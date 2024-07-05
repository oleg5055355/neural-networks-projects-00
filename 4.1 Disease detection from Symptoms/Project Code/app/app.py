from flask import Flask, render_template, request
import numpy as np
import os
from model import predict
#import seaborn as sns
#import matplotlib.pyplot as plt
#import pandas as pd

app = Flask(__name__)


UPLOAD_FOLDER = '/Users/adityavs14/Documents/Internship/Pianalytix/Month_2/sym2dis/app/static'
ALLOWED_EXTENSIONS = set(['png','jpg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER





@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        file1 = request.form['file1']
        s = predict(file1)
        if s:
            result = s
        else :
            result = ""
    return render_template('index.html',inp = file1, result=result) 





if __name__ == "__main__":
    app.run(debug=True)