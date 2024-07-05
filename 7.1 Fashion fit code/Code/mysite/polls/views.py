from django.shortcuts import render, redirect
import pandas as pd
import pickle

def index_func(request):
    res = 0
    if request.method == 'POST':
        name = request.POST['name']
        size= request.POST['size']
        cup = request.POST['cup']
        bra = request.POST['bra']
        category = request.POST['category']
        length = request.POST['length']
        fit = request.POST['fit']
        shoeSize = request.POST['shoeSize']
        shoeWidth = request.POST['shoeWidth']
        height = request.POST['height']

        if name != "":
            df = pd.DataFrame(columns=['size', 'cup size', 'bra size', 'category',
                                       'length', 'fit', 'shoe size', 'shoe width',
                                       'height_inches'])

            df2 = {'size': float(size), 'cup size': float(cup), 'bra size': float(bra), 'category':
                    float(category),'length': float(length), 'fit': float(fit), 'shoe size':
                    float(shoeSize), 'shoe width': float(shoeWidth),'height_inches': float(height)}

            df = df.append(df2, ignore_index=True)
            # load the model from disk
            filename1 = 'polls/Clothes.pickle'
            loaded_model = pickle.load(open(filename1, 'rb'))
            res = loaded_model.predict(df)
            print(res)

        else:
            return redirect('homepage')
    else:
        pass

    return render(request, "index.html", {'response': res})
