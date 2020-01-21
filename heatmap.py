'''
Created on Jan 20, 2020
Using Heat Map
@author: ashish
'''
# heat map
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.DataFrame(dict(categorical_1=['apple', 'banana', 'grapes',
                                      'apple', 'banana', 'grapes',
                                      'apple', 'banana', 'grapes'], 
                  categorical_2=['A','A','A','B','B','B','C','C','C'], 
                  value=[10,2,5,7,3,15,1,6,8]))
pivot_table = df.pivot("categorical_1", "categorical_2", "value")
# try printing out pivot_table to see what it looks like!
fig, ax = plt.subplots(figsize=(5,5))
sns.heatmap(data=pivot_table, 
            cmap=sns.color_palette("Blues"),
            ax=ax)

plt.show()
