#This program analysis.py
#- outputs a summary of each variable to a single text file.
#- saves a histogram of each variable to png files, and
# outputs a scatter plot of each pair of variables.

#I worked on each task seperatley and then put them all together.

#First a summary of the each variable saved to a single text file.

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

#data frame code for seperating each species from https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

#seperating them by species
setosa = data[data['species']=='setosa'] 

versicolor =data[data['species']=='versicolor']

virginica =data[data['species']=='virginica']

##summary of details to string for the txt file
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

#ref:
# lecture videos
# https://realpython.com/read-write-files-python/

#Saves a historgram of each variable to png files

#outputs histograms
setosa.hist()
versicolor.hist()
virginica.hist()

#saves each historgram to png files with their species title
plt.savefig("setosa.png")
plt.savefig("versicolor.png")
plt.savefig("virginica.png")

#note, you have to "x" out of histograms for scatter plots to appear

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
