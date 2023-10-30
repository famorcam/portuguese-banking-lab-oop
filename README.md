# README

## Project Intro/Objective
The purpose of this project is to engineer a pipeline to analyze stock data. Specifically, we have used the pipeline to calculate the mean, median and standard deviation of a data set comprised of 9 weeks of stock data. Following the completion of this pipeline, we will integrate text data in the form of news headlines, to determine how reliable sentiment can predict stock prices.

### Methods Used
* OOP
* Debugging

### Technologies
* Python

## Project Description
This project runs a validation script to test the correct output of steps 1-3. The primary challenge was in understanding how exactly how one manipulates the data structure into a format that can be used to satisfy each step; i.e. into a structure we can take the mean, median and std dev of. Each defined function uses a sequence of steps to properly format the data from a csv file to list of lists that we can work with. We must:

* drop the first element in each row of data 
* drop any missing values
* convert each element in each row from type String to type Float

The final step of each function is to execute code that satisfies either finding the mean, median, or standard deviation; dependent on each part of the project.

The most vital tool for this project was debugging. I primarily used print() statements to check if the changes I made led me one step closer to the end goal.

The most challenging aspect for me was figuring out how to make my code less verbose.