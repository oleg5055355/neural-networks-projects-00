from tensorflow import keras
import numpy as np
import cv2


base = '/Users/adityavs14/Documents/Internship/Pianalytix/Month_2/MusicSpectrometer/app'
model = keras.models.load_model(f'{base}/music.h5')
class_names = ['blues', 'classical', 'hiphop', 'pop', 'rock']
def image_pre(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (224,224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    data = (np.array(img).reshape(-1,224,224,3))
    return data

def predict(data):
    return class_names[np.argmax(model.predict(data)[0])]
