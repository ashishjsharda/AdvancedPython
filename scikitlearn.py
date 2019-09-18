'''
Created on Sep 18, 2019
Example using ScikitLearn
@author: asharda
'''
from sklearn.datasets import load_boston
import pandas as pd
boston = load_boston()
boston_data = pd.DataFrame(boston.data, columns=boston.feature_names)
print(boston_data.shape)
print(boston_data.head())
