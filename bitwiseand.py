'''
Created on Dec 30, 2019
Bitwise AND
@author: ashish
'''
import numpy as np
a,b=13,17
print("Binary of a seen is ",bin(a))
print("Binary of b seen is ",bin(b))
c=np.bitwise_and(a,b)
print("Bitwise and seen is ",c)
