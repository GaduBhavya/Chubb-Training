import requests
import pandas as pd
from flask import render_template,Flask,request
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/graph")
def graph():
    return render_template("graph.html")


def graph(x,y,xl,yl):
    fig = plt.figure()
    fig.set_figwidth(15)
    fig.set_figheight(15)
    plt.scatter(x,y)
    plt.xlabel(xl)
    plt.ylabel(yl)
    poly = np.poly1d(np.polyfit(x,y,3))
    line = np.linspace(1,35000000,1000)
    plt.plot(line,poly(line))
    plt.show()
    
def graph1(x,y,xl,yl):
    fig = plt.figure()
    fig.set_figwidth(15)
    fig.set_figheight(15)
    plt.scatter(x,y)
    plt.xlabel(xl)
    plt.ylabel(yl)
    poly = np.poly1d(np.polyfit(x,y,3))
    line = np.linspace(1,400000,1000)
    plt.plot(line,poly(line))
    plt.show()
    
def r_square(x,y):
    poly = np.poly1d(np.polyfit(x,y,3))
    return r2_score(y,poly(x))

def predict(x,y,value):
    poly = np.poly1d(np.polyfit(x,y,3))
    return poly(value)

if __name__ == '__main__':
    data = pd.read_csv('case_time_series.csv')


app.run(debug=True,port=5000)