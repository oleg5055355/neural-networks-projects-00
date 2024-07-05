import joblib

from pathlib import Path
import numpy as np
#from sklearn.preprocessing import LabelEncoder as lnc
import pandas as pd
import xgboost as xgb
import tensorflow
from tensorflow.keras import models


BASE_DIR = Path(__file__).resolve(strict=True).parent


model = models.load_model(f'{BASE_DIR}/recommendation.h5')
#xgb_r = xgb.Booster()
xgb_r = joblib.load(f'{BASE_DIR}/yield.joblib')
model.compile(loss='sparse_categorical_crossentropy',optimizer='adam')


features1 = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
features2 = ['Item', 'Year', 'average_rain_fall_mm_per_year', 'pesticides_tonnes','avg_temp']
def predict_pipe1(X):
    X = np.array(X).reshape(1,-1)
    lnc = joblib.load(f'{BASE_DIR}/recommendation_enc.joblib')
    pred = model.predict(X)
    return lnc.inverse_transform(np.array(np.argmax(pred)).reshape(1,-1))[0]


def predict_pipe2(l):
    l = np.array(l).reshape(1,-1)
    df = pd.DataFrame(l,columns=features2)
    lnc1 = joblib.load(f'{BASE_DIR}/yield_item.joblib')
    df['Item'] = lnc1.transform(df['Item'])
    X = df.values.reshape(1,-1)
    pred = xgb_r.predict(X)
    return pred[0]

    




