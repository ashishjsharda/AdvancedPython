'''
Created on Sep 19, 2019
Min Max Scaling
@author: asharda
'''
import numpy as np
import sklearn.preprocessing as preprocessing
input_data=([2,-1,5.5],
            [3.1,4.2,5.8],
            [1.3,5.7,3.8])
data_binarized=preprocessing.Binarizer(threshold=0.5).transform(input_data)
print(data_binarized)
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print ("\nMin max scaled data:\n", data_scaled_minmax)
