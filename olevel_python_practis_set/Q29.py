
# wright a python program find the odd numbers in array

import numpy as np

array= np.array([10,25,30,65,75,50,121])


for i in range(len(array)):
    if(array[i]%2==0):
        print(array[i],end=" ")