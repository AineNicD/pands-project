# pands-project
My GMIT Programming and Scripting Project 2020

## Introduction
This repository contains my research of the well known [Fisher’s Iris data set](https://en.wikipedia.org/wiki/Iris_flower_data_set) with written documentation and code in Python for my project. 
I downloaded the [irish data set](IrisDataSet.csv) from [github](https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv).

## Problem statement
This project concerns the well-known Fisher’s Iris data set. You must research the data set and write documentation and code (in Python to investigate it. An online search for information on the data set will convince you that many people have investigated it previously. You are expected to be able to break this project into several smaller tasks that are easier to solve, and to plug these together after they have been completed. You might do that for this project as follows: 
> 1. Research the data set online and write a summary about it in your README. 
> 2. Download the data set and add it to your repository. 
> 3. Write a program called analysis.py that: 
>
> • outputs a summary of each variable to a single text ﬁle, 
> • saves a histogram of each variable to png ﬁles, and 
> • outputs a scatter plot of each pair of variables. 

### Program solution: [analysis.py]()


## Technologies 

* [Cmder console emulator](https://cmder.net/), a pre-configured software package that provides you with a great terminal emulator.

* [Visual Studio Code](https://code.visualstudio.com/), this source-code editor will assist you in saving annd editing your code.

* [Anaconda](https://www.anaconda.com/distribution/), a free and open-source distribution of the Python programming language.
Anaconda is popular because it brings many of the tools used in data science and machine learning with just one install, so it's great for having short and simple setup. It has all the libraries needed to write and implement the programs in this project. 

A program to Check the versions of libraries in your Python Packages. [checkLibraries.py](https://github.com/AineNicD/pands-project/blob/master/checkLibraries.py)
Many of these libraries have data sets on them. Ready to be imported with the right code. 
Such as: [scikit-learn](https://scikit-learn.org/stable/)

~~~ ## Import data
from sklearn.datasets import load_iris 
iris_dataset = load_iris()

print(iris_dataset['DESCR'])
~~~
Another way is to use the [pandas](https://pandas.pydata.org/) 
for this, have the csv file in the same directory that your python process is based
~~~
#Load the Pandas libraries with alias 'pd' 
import pandas as pd 
# Read data from file 'filename.csv' 
data = pd.read_csv("IrisDataSet.csv") 
~~~

##### For Statistical Analysis code [ref](https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40)
Import all necessary libraries of Python —
~~~
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
~~~
Once you are sure you have the right software installed with the accompying library(I cannnot recomend Anaconda enough for this)
Get to know what you are working with.
* [Learnpython.org](https://www.learnpython.org/) is a great source for this.
For
* [pandas](https://pandas.pydata.org/)- pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,built on top of the Python programming language.
* [matplotlib](https://matplotlib.org/) Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python
* [seaborn](https://seaborn.pydata.org/) is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
* [numpy](https://numpy.org/) is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python.

Those websites are full of information about how to use the tools and is a great source for code.
Also a quick google search is sure to bring good results. 
I am new to Programming but even I can tell python is the best language.
There is so much support and it is all open source. [Python community](https://www.python.org/community/).


### About Fisher's Iris data set. 

The Iris flower data set is a multivariate data set. It consists of 50 samples from each of three species of Iris Flowers:

1 Iris Setosa

2 Iris Virginica 

3 Iris Versicolor

![](irisspecies.png)

Under 5 attributes;

* Petal Length
* Petal Width
* Sepal Length
* Sepal width 
* Species

![](petal_sepal.png)

It was introduced by the British statistician and biologist Ronald Fisher in his 1936 paper [“The use of multiple measurements in taxonomic problems”.](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x)


The Iris dataset is deservedly widely used throughout statistical science, especially for illustrating various problems in statistical graphics, multivariate statistics and machine learning.[ref](https://stats.stackexchange.com/questions/74776/what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching/74901#74901)
There are many reasons for this: 

* It contains 150 observations, it is small but not trivial. 
* There are no null values in the data set.
* There are 50 observations of each species (setosa, versicolor, virginica).[ref](https://stats.stackexchange.com/questions/74776/what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching/74901#74901)
* Anderson classified 50 examples of 3 different species. Each specimen was [ref](https://www.cs.odu.edu/~ccartled/Teaching/2017-Fall/DataAnalysis/Presentations/030-iris-dataset.pdf)
* Collected on the same day
* Collected by the same person
* Measured using the same instruments
* The task it poses of discriminating between three species of Iris from measurements of their petals and sepals is simple but challenging.
* The data are real good quality data. In principle and in practice, test datasets could be synthetic and that might be necessary or useful to make a point. 
* The Iris dataset can be enjoyably coupled with pictures of the flowers concerned, as from e.g. the useful [Wiki](https://en.wikipedia.org/wiki/Iris_flower_data_set) entry on the dataset.

![](iris.png)

###### note
Iris setosa, Iris versicolor and Iris virginica are three species (not varieties, as in some statistical accounts)[ref](https://stats.stackexchange.com/questions/74776/what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching/74901#74901)


#### Plots

To start the reseach of the data through plots, I created a histogram, scatterplot and boxplot to get a closer look at how the variables are represented. I got good help with this from [ref](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/). [hist-variable.py](https://github.com/AineNicD/pands-project/blob/master/hist-variable.py), [scattervariable.py](https://github.com/AineNicD/pands-project/blob/master/scattervariable.py) and [boxvariable.py](https://github.com/AineNicD/pands-project/blob/master/boxvariable.py).

I found my perfered method to load the iris data into my code is; 
~~~
import pandas as pd
data = pd.read_csv("IrisDataSet.csv") 
~~~
a reminder of other important imports;
~~~
import matplotlib.pyplot as plt
import numpy as np
~~~
![](hist-variable.png)
![](scattervariable.png)
![](boxvariable.png)

### researching the data set
From these plots, it is a bit dificult to understand the data. As they are from three different species all bunched into one.
I played around with different ways to seperate the data.
A type into google of the “iris data set” produced pages upon pages of codes and analysis of the data set. It was very useful to see other people’s findings. 
Many people broke the data down into seperate bits to analyse it further;
such as this code which gives you the first 20 lines. 
~~~
# head, number prints the number of lines you want
print(dataset.head(20))
~~~
from [Machine learning mastery](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/) this page also has a great break down of the data set and a few codes.

I decided to work with the data in full for my tasks but seperated them by speceis. 

I highly recommend [scilkit-learn](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html), it has great information on data sets already built in. 

I got a good code for seperating the data species from [Kaggle](https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation)
~~~
setosa =data[data['species']=='setosa']

versicolor =data[data['species']=='versicolor']

virginica =data[data['species']=='virginica']
~~~
I used this method to describe each variabe in [describe.py](https://github.com/AineNicD/pands-project/blob/master/Describe.py).
It produces a lovely output sumarising each species data.

![](Describe()output.png)

I used this summary of the data for my [Summarytxt.py](https://github.com/AineNicD/pands-project/blob/master/summaryTxt.py)

I added this code to output the summary of each variable to a single text file, 
~~~
a = setosa.describe(), versicolor.describe(),virginica.describe()

print(a)

#outputing result of code to a text file.
def out_fun():
    return str(a)
output = out_fun()
file = open("Summaryvariable.txt","w")
file.write(output)
file.close()
~~~

I got great help with this output code from [ref](https://www.quora.com/How-do-I-write-the-output-of-a-function-to-a-text-file-in-python)
I again seperated them by species. I improved on this code for my main [analysis.py]()

Next step was to save a histogram of each variable to png files,

I seperated them by species to produce histograms of each vaibale that save under the name of the species. 
[histVarPng.py]()
~~~
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
~~~

Setosa

![](setosa.png)

Versicolor

![](versicolor.png)

Virginica

![](virginica.png)

For outputing scatter plots of each pair of data. [scattervar.py](). 
These imports were used in this code
~~~
from pandas.plotting import scatter_matrix
import seaborn as sns
~~~
There are so many great codes for analysis in the Seaborn library
[seaborn website](https://seaborn.pydata.org/generated/seaborn.PairGrid.html)  helped me deveop this for the scatterplots of each pair,
 seaborn.FacetGrid is a Multi-plot grid for plotting conditional relationships.
After many failed attemps and playing around with it, I used this method to produce these two lines of code.
~~~
sns.FacetGrid(data, hue="species", height=6).map(plt.scatter, "sepal_length", "sepal_width").add_legend() 
sns.FacetGrid(data, hue="species", height=6).map(plt.scatter, "petal_length", "petal_width").add_legend() 
~~~
This output my scatter plots of each pair of variables. 

![](scatterSepal.png)
![](scatterPetal.png)

Now that I had finally figured out how to do the three tasks set out in this project it was time to put them all together in [analysis.py]()

I copy and pasted all three codes into one Visual studio code file and began working on it there, they went together well which I was happy about. 


### References
Ian McLoughlin and Andrew Beatty course material - They have done a great job of introducing a newbie like me to python coding and I watched and rewatched their video material many times while completing this project. They also provided great links to material for further learning which were of great help.

A whirlwind tour of python by Jake Vanderplas- in particular the chaper "A preview of data science tools" for this project

[Real Python matplotlib guide](https://realpython.com/python-matplotlib-guide/)

[Real Python read write files](https://realpython.com/read-write-files-python/)

[Wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set)

[iris data](https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv)

[medium](https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40)

[stats stack exchange](https://stats.stackexchange.com/questions/74776/what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching/74901#74901)

[cs.odu](https://www.cs.odu.edu/~ccartled/Teaching/2017-Fall/DataAnalysis/Presentations/030-iris-dataset.pdf)

[machine learning mastery](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)

[scikit-learn](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html)

[pandas dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html)

[stack over flow](https://stackoverflow.com/questions/46411533/how-can-i-save-histogram-plot-in-python)

[seaborn data](https://seaborn.pydata.org/generated/seaborn.PairGrid.htm)

