#This program saves the summary of the variables to a text file.

import numpy as np
import pandas as pd

#read data
data = pd.read_csv("irisDataSet.csv")

#names of variables
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

#data frame code for separating each species from https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

#seperating them by species
setosa = data[data['species']=='setosa'] 

versicolor =data[data['species']=='versicolor']

virginica =data[data['species']=='virginica']

#summary of details to string for the txt file
d = str(data.describe())
s = str(setosa.describe())
ver = str (versicolor.describe())
vir = str(virginica.describe())

#output to terminal
print ("IRIS DATA SET SUMMARY")
print (d)
print ("SETOSA DETAILS")
print(s)
print ("VERSICOLOR DETAILS")
print(ver)
print ("VIRGINICA DETAILS")
print(vir)

#output to file with headings on seperate lines
file = open("Summary.txt","w")
file.write(" IRIS DATA SET SUMMARY \n")
file.write(d)
file.write("\n SETOSA DETAILS \n")
file.write(s)
file.write("\n VERSICOLOR DETAILS \n")
file.write(ver)
file.write("\n VIRGINICA DETAILS \n")
file.write(vir)
file.close()
