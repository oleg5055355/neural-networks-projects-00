from flask import Flask, render_template, request
import model.model as m

app = Flask(__name__)
@app.route("/", methods = ["GET","POST"])
def start():
    return render_template('index.html')


@app.route("/recommend", methods = ["GET","POST"])
def hello1():
    l1=[]
    if request.method == "POST":
        for i in m.features1:
            try:
                l1.append(float(request.form[i]))
            except ValueError:
                l1.append(request.form[i])
        recommendation = m.predict_pipe1(l1)
    else:
        recommendation = ''



    return render_template('index.html', rec=recommendation)

@app.route("/yield", methods = ["GET","POST"])
def hello2():
    l2=[]
    if request.method == "POST":
        for i in m.features2:
            try:
                l2.append(float(request.form[i]))
            except ValueError:
                l2.append(request.form[i])
        yi = m.predict_pipe2(l2)
    else:
        yi = 0



    return render_template('index.html', yie=yi)




if __name__ == "__main__":
    app.run(debug=True)