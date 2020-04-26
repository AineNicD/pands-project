import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("IrisDataSet.csv") 


# scatter plot matrix
from pandas.plotting import scatter_matrix
scatter_matrix(data)
plt.show()

#https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
