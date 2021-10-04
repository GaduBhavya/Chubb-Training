# PROGRAM : day11 task1
# PROGRAMMED By  : Bhavya Yasaswini Gadu
# Email-id : GaduBhavya.Yasaswini@Chubb.com
# Date : 30-sep-2021
# Python Version : 3.7.3
# Caveats : None
# License : None

'''
Write a python program to calulate geometric mean and harmonic mean of a dataset
'''

import math

def geometric_mean(data):
    product = 1
    for i in data:
        product*=i
    return math.pow(product,(1/len(data)))

def harmonic_mean(data):
    inverse_sum = 0
    for i in data:
        inverse_sum+=(1/i)
    return len(data)/inverse_sum

data = list(map(int,input().split()))
gm = geometric_mean(data)
hm = harmonic_mean(data)
print("Geometric mean =",gm)
print("Harmonic mean =",hm)