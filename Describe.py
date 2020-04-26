#A code to describe each data set variable 
import numpy as np
import pandas as pd

#read data
data = pd.read_csv("irisDataSet.csv")

#names of variables
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/
# Pandas describe() is used to view some basic statistical details like percentile,
# mean, std etc. of a data frame or a series of numeric values. 

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
# DataFrame.describe(percentiles=None, include=None, exclude=None)[source]

setosa=data[data['species']=='setosa']

versicolor =data[data['species']=='versicolor']

virginica =data[data['species']=='virginica']

print ("setosa")
print(setosa.describe())

print ("versicolor")
print(versicolor.describe())

print ("virginica")
print(virginica.describe())


# print(data.describe())

