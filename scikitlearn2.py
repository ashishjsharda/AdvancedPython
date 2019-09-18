'''
Created on Sep 18, 2019
Example using ScikitLearn
@author: asharda
'''
from sklearn.datasets import load_diabetes
import pandas as pd
diabetes=load_diabetes()
diabetes_data=pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
print(diabetes_data.head(5))

