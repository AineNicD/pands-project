#A summary of the each variable saved to a single text file.

#The method I learned to output to a text file was for strings, I used str() to incorporate it here.
#This code saves the summary of the variables to a text file but I would prefer the text file 
#be a bit more pleasant to look at. 

import numpy as np
import pandas as pd

#read data
data = pd.read_csv("irisDataSet.csv")

#names of variables
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
# DataFrame.describe(percentiles=None, include=None, exclude=None)[source]

setosa data[data['species']=='setosa'] 

versicolor =data[data['species']=='versicolor']

virginica =data[data['species']=='virginica']

#changing them all to one line as str() will only accept one.
#changing them all to one line as str() will only accept one.
a = setosa.describe(), versicolor.describe(),virginica.describe()

print(a)

#str converts whatever you pass in to a string.
def out_fun():
    return str(a)
output = out_fun()
file = open("Summaryvariable.txt","w")
file.write(output)
file.close()
