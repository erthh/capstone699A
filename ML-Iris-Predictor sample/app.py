from flask import Flask,render_template,url_for,request
from flask_material import Material

# EDA Package
import pandas as pd 
import numpy as np

# ML Package
from sklearn.externals import joblib

app = Flask(__name__)
Material(app) # Pass Flask-Material into APP 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/preview')
def preview():
    df = pd.read_csv("data/iris.csv")
    return render_template("preview.html" , df_view = df) # send df_view(csv file) to preview.html

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        petal_length = request.form['petal_length']
        sepal_length = request.form['sepal_length']
        petal_width = request.form['petal_width']
        sepal_width = request.form['sepal_width']
        Input1 = request.form['Input1']
        Input2 = request.form['Input2']
        Input3 = request.form['Input3']
        Input4 = request.form['Input4']

    return render_template("index.html",sepal_length=sepal_length , Input1 = Input1 , Input2=Input2
    ,Input3 = Input3,Input4 = Input4, petal_length=petal_length,petal_width=petal_width,sepal_width=sepal_width) #Send sepal_length back to index.html to use type {{sepal_length}}

if __name__ == '__main__':
    app.run(debug=True)

print('hello')