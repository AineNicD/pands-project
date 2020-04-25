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

It might help to suppose that your manager has asked you to investigate the data set, with a view to explaining it to your colleagues. Imagine that you are to give a presentation on the data set in a few weeks’ time, where you explain what investigating a data set entails and how Python can be used to do it. You have not been asked to create a deck of presentation slides, but rather to present your code and its output to them.

## Technologies for this research project

* [Cmder console emulator](https://cmder.net/), a pre-configured software package that provides you with a great terminal emulator.

* [Visual Studio Code](https://code.visualstudio.com/), this source-code editor will assist you in saving annd editing your code.

* [Anaconda](https://www.anaconda.com/distribution/), a free and open-source distribution of the Python programming language.
Anaconda is popular because it brings many of the tools used in data science and machine learning with just one install, so it's great for having short and simple setup. It has all the libraries needed to write and implement the programs in this project. 

A program to Check the versions of libraries in your Python Packages. [checkLibraries.py](https://github.com/AineNicD/pands-project/blob/master/checkLibraries.py)


### About Fisher's Iris data set. 

![](petal_sepal.png)

The Iris flower data set is a multivariate data set. It consists of 50 samples from each of three species of Iris Flowers — Iris Setosa, Iris Virginica and Iris Versicolor, under 5 attributes - Petal Length, Petal Width, Sepal Length, Sepal width and Class(Species).
It was introduced by the British statistician and biologist Ronald Fisher in his 1936 paper [“The use of multiple measurements in taxonomic problems”.](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x)

![](irisspecies.png)

![](iris.png)

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

###### note
Iris setosa, Iris versicolor and Iris virginica are three species (not varieties, as in some statistical accounts)[ref](https://stats.stackexchange.com/questions/74776/what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching/74901#74901)


