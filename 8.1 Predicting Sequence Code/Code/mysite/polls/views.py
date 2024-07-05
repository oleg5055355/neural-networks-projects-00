from django.shortcuts import render, redirect
from tensorflow.keras.models import load_model
import numpy as np

# Create your views here.
def handler(request):
    result = [None]
    if request.method == 'POST':
        sequence = request.POST['Name']
        result = predicting(preprocessing(sequence))
    else:
        pass
    return render(request, "index.html", {'response': result[0]})


def predicting(data):
    # Loading the Neural Network from disk.
    model = load_model("polls/NumberSequence.h5")
    result = model.predict(data)
    return result


def preprocessing(s):
    s_ = s.strip('][').split(', ')
    s_ = [int(x) for x in s_]
    s_new = np.array(s_)
    s_new = s_new.reshape((1, 7, 1))
    return s_new