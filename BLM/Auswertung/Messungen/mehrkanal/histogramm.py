#!/usr/bin/python2
import numpy as np, matplotlib.pyplot as plt
import scipy.optimize as opt 


# plotte histogramm
data = np.loadtxt("mehrkanal.DAT")
hist, bins = np.histogram(data, bins=30, range = [data.min(),data.max()-1] )

# zeichne histogramm 

plt.grid(True) # zeichne koordinatengitter
plt.xlabel(r"Strom (pA)")
plt.ylabel(r"Haeufigkeit")

plt.bar(bins[:-1],hist)


plt.show()
