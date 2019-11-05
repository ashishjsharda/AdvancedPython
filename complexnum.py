'''
Created on Nov 4, 2019
Find Complex Numbers 
@author: asharda
'''
import numpy as np 
a = np.array([1, 2+6j, 5, 3.5+5j])
print(a[np.iscomplex(a)]) 
