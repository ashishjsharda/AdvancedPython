'''
Split Lines using Line Boundary
'''
import numpy as np
print(np.char.splitlines('hello\nhow are you'))
print(np.char.splitlines('Hello\rHow are you'))
