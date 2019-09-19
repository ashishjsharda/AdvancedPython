from sklearn.datasets import load_breast_cancer
data=load_breast_cancer()
print(data)
label_names=data['target_names']
print(label_names)
label=data['target']
print(label)
fetaure_names=data['feature_names']
print(fetaure_names)
