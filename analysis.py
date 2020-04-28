#This program analysis.py
#- outputs a summary of each variable to a single text file.
#- saves a histogram of each variable to png files, and
# outputs a scatter plot of each pair of variables.

#I worked on each task seperatley and then put them all together.

#First a summary of the each variable saved to a single text file.

#The method I learned to output to a text file was for strings, I used str() to incorporate it here.
#This code saves the summary of the variables to a text file but I would prefer the text file 
#be a bit more pleasant to look at. 

import numpy as np
import pandas as pd

#https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html
# imported for scatter plot, there are many options like this in the pandas library
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns

#read data
data = pd.read_csv("irisDataSet.csv")

#names of variables
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

#seperating them by species
setosa = data[data['species']=='setosa'] 

versicolor =data[data['species']=='versicolor']

virginica =data[data['species']=='virginica']

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


#Saves a historgram of each variable to png files
#names of variables
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
# DataFrame.describe(percentiles=None, include=None, exclude=None)[source]
setosa =data[data['species']=='setosa']

versicolor =data[data['species']=='versicolor']

virginica =data[data['species']=='virginica']

# seperated each data by species
a = setosa
b= versicolor
c = virginica

#outputs histograms
a.hist()
b.hist()
c.hist()

#saves each historgram to png files with their species title
plt.savefig("setosa.png")
plt.savefig("versicolor.png")
plt.savefig("virginica.png")


plt.show()


# https://www.kaggle.com/farheen28/iris-dataset-analysis-using-knn
#https://seaborn.pydata.org/generated/seaborn.PairGrid.html
#Seaborn, there are so many great codes for analysis in the Seaborn library
#The links above helped me deveop this for the scatterplots of each pair
#after a few failed attemps and playing around with it,
#it simplified to two lines of code for both.

sns.FacetGrid(data, hue="species", height=8).map(plt.scatter, "sepal_length", "sepal_width").add_legend() 
sns.FacetGrid(data, hue="species", height=8).map(plt.scatter, "petal_length", "petal_width").add_legend() 

plt.show()

#https://www.kaggle.com/anthonyhills/classifying-species-of-iris-flowers