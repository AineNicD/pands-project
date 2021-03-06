#Aine Nic Dhonnacha
#This program analysis.py

#-outputs a summary of each variable to a single text file.
#-saves a histogram of each variable to png files, and
#outputs a scatter plot of each pair of variables.

#I worked on each task separately and then put them all together.

#import libraries 
import numpy as np
import pandas as pd
#https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html
#imported for scatter plot, there are many options like this in the pandas library
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

#summary of details to string for the text file
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


#outputs histograms
setosa.hist()
versicolor.hist()
virginica.hist()

#saves each historgram to png files with their species title
plt.savefig("setosa.png")
plt.savefig("versicolor.png")
plt.savefig("virginica.png")

#outputs scatter plots of each pair of variables

#https://www.kaggle.com/farheen28/iris-dataset-analysis-using-knn
#https://seaborn.pydata.org/generated/seaborn.PairGrid.html
#There are so many great codes for analysis in the Seaborn library
#The links above helped me deveop this for the scatterplots of each pair

sns.FacetGrid(data, hue="species", height=8).map(plt.scatter, "sepal_length", "sepal_width").add_legend() 
sns.FacetGrid(data, hue="species", height=8).map(plt.scatter, "petal_length", "petal_width").add_legend() 

#outputs plots
plt.show()

#references
#Ian McLoughlin course lecture videos
#https://www.kaggle.com/anthonyhills/classifying-species-of-iris-flowers
#https://realpython.com/read-write-files-python/
#https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
#https://www.kaggle.com/farheen28/iris-dataset-analysis-using-knn
