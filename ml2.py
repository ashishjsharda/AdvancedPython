from pandas import read_csv

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['alength', 'awidth', 'plength', 'pwidth', 'class']
dataset=read_csv(url,names=names)
print(dataset.head(20))
