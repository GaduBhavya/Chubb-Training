import numpy as np
import math
import json

num=np.arange(10,10001)
factorial = []
karprekar = []
for i in num:
    factorial.append(math.factorial(i))
factorial = np.array(factorial)

for i in num:
    square = str(i*i)
    for j in range(1,len(square)):
        part1 = int(square[:j])
        part2 = int(square[j:])
        if((part1+part2 == i) and (part1!=0) and (part2!=0)):
            karprekar.append(i)
karprekar = np.array(karprekar)

json_obj = {"factorial":factorial,"karprekar":karprekar}
print(json_obj)