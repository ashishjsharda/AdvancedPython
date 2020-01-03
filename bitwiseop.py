'''
Created on Jan 3, 2020
Bitwise operations using numpy
@author: ashish
'''
import numpy as np
a,b=13,17
print(bin(a))
print(bin(b))
bit_and=np.bitwise_and(a,b)
print('Bitwise AND seen is',bit_and)
bit_or=np.bitwise_or(a,b)
print('Bitwise OR seen is',bit_or)
bit_xor=np.bitwise_xor(a,b)
print('Bitwise XOR seen is',bit_xor)

