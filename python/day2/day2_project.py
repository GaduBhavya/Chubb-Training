# PROGRAM : A basic python file
# PROGRAMMED By  : Bhavya Yasaswini Gadu
# Email-id : GaduBhavya.Yasaswini@Chubb.com
# Date : 17-sep-2021
# Python Version : 3.7.3
# Caveats : None
# License : None

'''
Create a python code which does the following:

1. Take a 4 digit numbernon-repeating number and arrange it in ascending and descending order to get two new numbers.
2. Now, subtract the highest number from lowest number till you get the number 6147
3. If the end result is 6147 then return True else False
'''

n=input()
a=[n]
if(len(list(n))!=len(set(n))):
    print('False')
else:
    while(1):
        l=list(str(n))
        l.sort()
        minimum="".join(l)
        maximum=minimum[::-1]
        n=int(maximum)-int(minimum)
        if(n == 6174):
            print('True')
            break
        elif n in a:
            print('False')
            break
        else:
            a.append(n)
