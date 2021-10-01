import requests
import json
from pymongo import MongoClient
from flask import render_template
from flask import Flask
from flask import render_template,jsonify,request


app = Flask(__name__)

url="https://api.thedogapi.com/v1/breeds"

class task:

    connection = MongoClient("mongodb://localhost:27017")

    def check_url(self,url):
        try:
            url = requests.get(url)
            return True
        except:
            return False


    def read_url(self,url):
        url = requests.get(url)
        return url.json()

    def create_json(self,data):
        with open("dogs.json","w") as file:
            return json.dump(data,file)

    def read_json(self,file):
        with open(file) as file:
            return json.load(file)

    def get_date(self,json_data):
        data = []
        for item in json_data:
            dict={}
            if "breed_group" in item.keys():
                dict["breed"] = item["breed_group"]
            else:
                dict["breed"] = 'Not available'
            if "origin" in item.keys():
                dict["country_of_origin"] = item['origin']
            else:
                dict["country_of_origin"] = 'Not available'
            if "bred_for" in item.keys():
                dict["bred_for"] = item['bred_for']
            else:
                dict["bred_for"] = 'Not available'
            if "image" in item.keys():
                dict["image"] = item['image']['url']
            else:
                dict["image"] = 'Not available'
            data.append(dict)
        return data

    def connect(self):
        if self.connection:
            return True
        else:
            return False

    def create_collection(self,db_name,collection):
        db_name = self.connection[db_name]
        new_collection = db_name[collection]
        return collection

    def insert_data(self,db_name,collection_name,data):
        self.connection[db_name][collection_name].insert_many(data)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/display")
def start():
    return render_template("display.html",name = data)


if __name__ == '__main__':

    obj = task()
    if obj.check_url(url):
        data = obj.read_url(url)
        obj.create_json(data)
        json_data = obj.read_json("dogs.json")
        data = obj.get_date(json_data)
        if obj.connect():
            obj.create_collection("chubb4","week1")
            obj.insert_data("chubb4","week1",data)

    app.run(debug=True,port=5000)
    

        
