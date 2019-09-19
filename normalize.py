import sklearn.preprocessing as preprocessing
input_data=([2,-1,5.5],
            [3.1,4.2,5.8],
            [1.3,5.7,3.8])
#Normalize the data
normalize=preprocessing.normalize(input_data,norm='l2')
print(normalize)
