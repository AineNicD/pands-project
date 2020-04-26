
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("IrisDataSet.csv") 
# box and whisker plots
data.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

#https://copycoding.com/d/your-second-machine-learning-project-with-this-famous-iris-dataset-in-python-part-5-of-9-