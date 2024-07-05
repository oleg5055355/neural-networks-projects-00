from tensorflow import keras
import numpy as np
import cv2
from pyrsgis import raster
from osgeo import gdal, gdal_array
from pyrsgis.convert import changeDimension
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

base = '/Users/adityavs14/Documents/Internship/Pianalytix/Month_2/Builtup/app'
model = keras.models.load_model(f'{base}/builtup.h5')


def image_pre(path):
    test = gdal.Open(path, gdal.GA_ReadOnly)
    testimage = np.zeros((test.RasterYSize, test.RasterXSize, test.RasterCount),
                gdal_array.GDALTypeCodeToNumericTypeCode(test.GetRasterBand(1).DataType))

    for b in range(testimage.shape[2]):
        testimage[:, :, b] = test.GetRasterBand(b+1).ReadAsArray()

    new_shape = (testimage.shape[0] * testimage.shape[1], testimage.shape[2])
    x_test = testimage[:, :, :6].reshape(new_shape)
    x_test=ss.fit_transform(x_test)
    #print(testimage[:,:,0].shape)
    return x_test, testimage[:,:,0].shape

def predict(data,shape):
    prediction = model.predict(data,verbose=1)

    out = np.round(prediction*255)
    out = out.reshape(shape)
    return out
