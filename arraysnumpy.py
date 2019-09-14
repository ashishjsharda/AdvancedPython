import numpy as np
num1=np.array([[1,2],[3,4],[5,6]])
#Print the shape of the matrix
print(np.shape(num1))
#Re-arrange rows and columns
newnum=num1.reshape(2,3)
print("New num seen is ",newnum)
