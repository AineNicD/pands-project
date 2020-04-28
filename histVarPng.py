#Saves a historgram of each variable to png files 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#read data
data = pd.read_csv("irisDataSet.csv")

#names of variables
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# seperating by species
setosa =data[data['species']=='setosa']

versicolor =data[data['species']=='versicolor']

virginica =data[data['species']=='virginica']

#outputs histograms
setosa.hist()
versicolor.hist()
virginica.hist()

#saves each historgram to png files with their species title
plt.savefig("setosa.png")
plt.savefig("versicolor.png")
plt.savefig("virginica.png")


plt.show()


# Ian Mc Loughlin lecture on plots
#data frame code for each species from https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

