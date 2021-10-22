import requests
import pandas as pd
from flask import render_template,Flask,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",name = data)

@app.route("/graph")
def graph():
    return render_template("graph.html")

@app.route("/analysis")
def analysis():
    return render_template("analysis.html")

if __name__ == '__main__':
    data = pd.read_csv('data_2.csv')

app.run(debug=True,port=5000)