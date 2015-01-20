#!/usr/bin/python2
import numpy as np

# read in file line by line and copy it into datalist, which is a list where each element is a line which again is a list of elements
file = open("FieldInhomogenities.txt", "r")
datalist = []
for line in file:
    if line.strip().split(" ")[0] != "#": # strip cleans whitespace from start and end of line, split converts lines into lists
        datalist +=(line.strip().split(" "))[1:-1] # append list representing line to datalist
datalist = np.array(datalist, dtype=float)
print datalist, "\n"
print "relative error: ", np.std(datalist)/np.mean(datalist)








        

