
# wright a python function to get two matrices and multiply them make sure that number of first matrix = number of rows of second

import numpy as np

a=[[1,2,3],[2,1,3],[4,6,2]]

b=[[7,2,4],[5,3,1],[1,2,4]]

c=[[0,0,0],[0,0,0],[0,0,0]]

c=np.dot(a,b)

for i in c:
    print(i)