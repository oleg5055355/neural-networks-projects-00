import keras
import numpy as np
from matplotlib.pyplot import imshow
from PIL import Image, ImageOps


base = '/Users/adityavs14/Documents/Internship/Pianalytix/Month_2/WeedDetection/app'
model = keras.models.load_model(f'{base}/WeedDetect.h5')

def image_pre(path):
    print(path)
    data = np.ndarray(shape=(1,128, 128, 3), dtype=np.float32)
    size = (128,128)
    image = Image.open(path)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    data = image_array.reshape((-1,128,128,3))/255
    return data,image

def predict(data):
    prediction = model.predict(data)
    return np.argmax(model.predict(data))
