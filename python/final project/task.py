import requests
from flask import render_template
from flask import Flask
from flask import render_template,jsonify,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/graphs')
def graphs():
    return render_template('graphs.html')

@app.route('/preprocess')
def preprocess():
    return render_template('preprocess.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000)

