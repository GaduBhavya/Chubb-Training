# PROGRAM : day11 task2
# PROGRAMMED By  : Bhavya Yasaswini Gadu
# Email-id : GaduBhavya.Yasaswini@Chubb.com
# Date : 30-sep-2021
# Python Version : 3.7.3
# Caveats : None
# License : None


'''
Write a program to calculate variance of a population
'''


def variance(data):
    mean = sum(data)/len(data)
    total = 0
    for i in data:
        total+=(i-mean)*(i-mean)
    return total/len(data)

data = list(map(int,input().split()))
var = variance(data)
print("Variance =",var)