# PROGRAM : day12 task1
# PROGRAMMED By  : Bhavya Yasaswini Gadu
# Email-id : GaduBhavya.Yasaswini@Chubb.com
# Date : 1-oct-2021
# Python Version : 3.7.3
# Caveats : None
# License : None


'''
You have given an api endpoint https://api.thedogapi.com/v1/breeds create a pandas dataframe with the endpoint
'''

import requests
import json
import pandas as pd

url="https://api.thedogapi.com/v1/breeds"

class dataframe:
    def check_url(self,url):
        try:
            url = requests.get(url)
            return True
        except:
            return False

    def read_url(self,url):
        url = requests.get(url)
        return url.json()

    def create_dataframe(self,data):
        data0 = pd.json_normalize(data[0])
        df = pd.DataFrame(data0)
        data = data[1:]
        for i in data:
            df1 = pd.json_normalize(i)
            df = pd.concat([df,df1])
        return df

d = dataframe()
if d.check_url(url):
    data = d.read_url(url)
    data1 = d.create_dataframe(data)
    print(data1)