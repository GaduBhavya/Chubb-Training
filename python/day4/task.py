# PROGRAM : day4 assignment
# Programmed by : Bhavya Yasaswini Gadu
# Email-id : GaduBhavya.Yasaswini@Chubb.com
# Date : 21-sept-2021
# Python Version : 3.7.3
# Caveats : None
# License : None

import json
from pymongo import MongoClient

class MJson:
    connection = MongoClient("mongodb://localhost:27017")

    def read_json(self,file):
        with open(file) as file:
            return json.load(file)

    def connect(self):
        if self.connection:
            return True
        return False

    def create_collection(self,db_name, collection):
        db_name = self.connection[db_name]
        collection = db_name[collection]
        return collection
    
    def insert_data(self, db_name, collection_name, data):
        self.connection[db_name][collection_name].insert_one(data)

if __name__ == '__main__':
    m = MJson()
    m.connect()
    m.create_collection("chubb4","student")
    data = m.read_json("day4/student.json")
    for i in data:
        m.insert_data("chubb4","student",i)
    
    