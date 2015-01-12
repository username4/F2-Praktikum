#!/usr/bin/python2
import numpy as np

# read in file line by line and copy it into datalist, which is a list where each element is a line which again is a list of elements
file = open("FieldInhomogenities.txt", "r")
datalist = []
for line in file:
    if line.strip().split(" ")[0] != "#": # strip cleans whitespace from start and end of line, split converts lines into lists
        datalist.append(line.strip().split(" ")) # append list representing line to datalist
# convert datalist to numpy array of floats        
datalist = np.array(datalist, dtype=float)

d = [line[0] for line in datalist]
UArray = [line[1:5] for line in datalist]

print "Array of voltages, 4 at each distance (mV)"
for line in UArray:
    print line

Uerrors = [np.std(line)/float(np.mean(line)) for line in UArray]
print "\nRelative errors for the mean dU/U for different distances (mV)"
for Uerror in Uerrors:
    print Uerror

meanUerror =  np.mean(Uerrors)
print "\nmean relative error <dU/U> = <dB/B>"
print "===>", meanUerror






        

