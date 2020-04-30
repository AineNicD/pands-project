import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Reading Iris Dataset in Pandas Dataframe
data = pd.read_csv("IrisDataSet.csv")
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']


# https://www.kaggle.com/farheen28/iris-dataset-analysis-using-knn
#https://seaborn.pydata.org/generated/seaborn.PairGrid.html
#seaborn, there are so many great codes for analysis in the Seaborn library
#The links above helped me develop this for the scatterplots of each pair
#after a few failed attempts and playing around with it,
#it simplified to two lines of code for both.

sns.FacetGrid(data, hue="species", height=6).map(plt.scatter, "sepal_length", "sepal_width").add_legend() 
sns.FacetGrid(data, hue="species", height=6).map(plt.scatter, "petal_length", "petal_width").add_legend() 

plt.show()

#https://www.kaggle.com/anthonyhills/classifying-species-of-iris-flowers
