import pandas as pd
import numpy as np
ser=pd.Series(np.arange(4.),index=['red','yellow','orange','blue'])
print(ser)
#Delete an item from series
print("Modified series is ",ser.drop('yellow'))
