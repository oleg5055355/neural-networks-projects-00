from django.shortcuts import render, redirect
import pandas as pd
import pickle
import os

def index_func(request):
    res = 0
    if request.method == 'POST':
        if request.POST.get('pred_button'):
            name = request.POST['Name']
            yor = request.POST['yor']
            NA = request.POST['NA']
            EU = request.POST['EU']
            JP= request.POST['JP']
            score = request.POST['score']
            critic_count = request.POST['critic_count']
            user_count = request.POST['user_count']
            console = request.POST['console']
            dev = request.POST['dev']
            rate = request.POST['rate']
            pub= request.POST['pub']

            if name != "":
                df = pd.DataFrame(columns=['Year_of_Release', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Critic_Score',
                                    'Critic_Count', 'User_Count', 'PC', 'PS2', 'PS3', 'X360',
                                    'other_console', 'Capcom', 'EA', 'Komani', 'Ubisoft', 'other_dev', 'E',
                                    'E10+', 'M', 'T', 'other_rating', 'Activision', 'Electronic Arts',
                                    'Konami Digital Entertainment', 'Nintendo',
                                    'Sony Computer Entertainment', 'Ubisoft', 'other_publisher'])

                # helper functions:
                console = console_func(console)
                dev = dev_func(dev)
                pg_rate = rate_func(rate)
                pub = pub_func(pub)

                df2 = {'Year_of_Release': int(yor), 'NA_Sales': float(NA), 'EU_Sales': float(EU),
                       'JP_Sales': float(JP), 'Critic_Score': float(score), 'Critic_Count': float(critic_count)
                       , 'User_Count': int(user_count), 'PC': console[0], 'PS2': console[1], 'PS3':
                        console[2], 'X360': console[3], 'other_console': console[4], 'Capcom': dev[0],
                       'EA': dev[1], 'Komani': dev[2], 'Ubisoft': dev[3], 'other_dev': dev[4], 'E': pg_rate[0]
                        ,'E10+': pg_rate[1], 'M': pg_rate[2], 'T': pg_rate[2], 'other_rating': pg_rate[2],
                       'Activision': pub[0], 'Electronic Arts': pub[1], 'Konami Digital Entertainment':
                        pub[2], 'Nintendo': pub[3], 'Sony Computer Entertainment': pub[4],
                       'Ubisoft': pub[5], 'other_publisher': pub[6]}

                df = df.append(df2, ignore_index=True)
                # load the model from disk
                filename = 'polls/VideoGamesModel.pickle'
                loaded_model = pickle.load(open(filename, 'rb'))
                res = loaded_model.predict(df)
                res = float(abs(res))
        else:
            return redirect('homepage')
    else:
        pass

    return render(request, 'index.html', {'result': res})


def console_func(x):
    # PC	PS2	PS3	X360	other_console
    if x == 'PC':
        return [1, 0, 0, 0, 0]
    elif x == 'PS2':
        return [0, 1, 0, 0, 0]
    if x == 'PS3':
        return [0, 0, 1, 0, 0]
    if x == 'X360':
        return [0, 0, 0, 1, 0]
    else:
        return [0, 0, 0, 0, 1]


def dev_func(x):
    # Capcom	EA	Komani	Ubisoft	other_dev
    if x == 'Capcom':
        return [1, 0, 0, 0, 0]
    elif x == 'EA':
        return [0, 1, 0, 0, 0]
    if x == 'Komani':
        return [0, 0, 1, 0, 0]
    if x == 'Ubisoft':
        return [0, 0, 0, 1, 0]
    else:
        return [0, 0, 0, 0, 1]


def rate_func(x):
    # E	E10+	M	T	other_rating
    if x == 'E':
        return [1, 0, 0, 0, 0]
    elif x == 'E10+':
        return [0, 1, 0, 0, 0]
    if x == 'M':
        return [0, 0, 1, 0, 0]
    if x == 'T':
        return [0, 0, 0, 1, 0]
    else:
        return [0, 0, 0, 0, 1]


def pub_func(x):
    # Activision, Electronic Arts, Konami Digital Entertainment, Nintendo,
    # Sony Computer Entertainment, Ubisoft, other_publisher
    if x == 'Activision':
        return [1, 0, 0, 0, 0, 0, 0]
    elif x == 'Electronic Arts':
        return [0, 1, 0, 0, 0, 0, 0]
    if x == 'Konami Digital Entertainment':
        return [0, 0, 1, 0, 0, 0, 0]
    if x == 'Nintendo':
        return [0, 0, 0, 1, 0, 0, 0]
    elif x == 'Sony Computer Entertainment':
        return [0, 0, 0, 0, 1, 0, 0]
    elif x == 'Ubisoft':
        return [0, 0, 0, 0, 0, 1, 0]
    else:
        return [0, 0, 0, 0, 0, 0, 1]
