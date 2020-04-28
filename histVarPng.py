#Saves a historgram of each variable to png files 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#read data
data = pd.read_csv("irisDataSet.csv")

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

#I found the quick method to save each histogram from https://stackoverflow.com/questions/46411533/how-can-i-save-histogram-plot-in-python


plt.show()





