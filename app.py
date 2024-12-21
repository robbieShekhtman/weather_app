from flask import Flask, render_template, request
from weather import main as getData

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    data = None
    if request.method == "POST":
        city = request.form['cityName']
        data = getData(city)
    return render_template('index.html', data = data)

if __name__ == '__main__':
    app.run(debug=True) 