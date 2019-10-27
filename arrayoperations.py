'''
Created on Oct 27, 2019
Array Operations using numpy
@author: asharda
'''

import numpy as np
list1=[10,12,14,16]
arr=np.array(list1)
print(arr)
arr=arr+2
print(arr)
print("Max seen is ",arr.max())
print("Min seen is ",arr.min())
print("Cumulative sum seen is ",np.cumsum(arr))

