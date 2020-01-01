'''
Created on Jan 1, 2020
Array Operations using Numpy
@author: ashish
'''
import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
mul=np.multiply(a,b)
print("Multiply a and b ",mul)
add=np.add(a,b)
print("Addition of a and b is",add)
sub=np.subtract(b,a)
print("Substraction of b and a is",sub)
div=np.divide(b,a)
print("Division of b and a is",div)

