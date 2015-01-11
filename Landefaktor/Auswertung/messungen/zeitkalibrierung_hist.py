#!/usr/bin/python2

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data=np.loadtxt("Kalibration.RPT")


plt.figure()


plt.grid()
plt.xlabel(r"Channel (#)")
plt.ylabel(r"counts")


plt.step(data[:,0],data[:,1])
plt.savefig("zeitkalibrierung_hist.pdf") # plots besser als vektorgrafik speichern, also pdf oder 

plt.show()
