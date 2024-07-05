from tensorflow import keras
import numpy as np
from matplotlib.pyplot import imshow
import cv2
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import plotly.express as px


base = '/Users/adityavs14/Documents/Internship/Pianalytix/NumberPlate/app'
model = keras.models.load_model(f'{base}/NPD.h5')

def image_pre(path):
    #print(path)
    img_arr = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    h,w,d = img_arr.shape
    load_image = load_img(path,target_size=(224,224))
    load_image_arr = img_to_array(load_image)
    norm_load_image_arr = load_image_arr/255.0
    X = np.array(norm_load_image_arr,dtype=np.float32).reshape(-1,224,224,3)
    return X,w,h

def predict(data,w,h):
    prediction = model.predict(data)
    xmin = prediction[0][0] * w
    xmax = prediction[0][1] * w
    ymin = prediction[0][2] * h
    ymax = prediction[0][3] * h
    return xmin,xmax,ymin,ymax
