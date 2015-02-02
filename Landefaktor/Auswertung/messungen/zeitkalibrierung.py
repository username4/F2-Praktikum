#!/usr/bin/python2

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

channels = np.array([17, 50, 84, 117, 151, 184, 217, 250, 284, 317, 351, 384, 418, 450, 484])
times = np.arange(1,16)

def linfunc(x, m, b):
    return m * x + b

popt, pcov = curve_fit(linfunc, channels, times)

plt.figure(1, [9,6])
plt.plot(channels, times, "bo",
         label="Messwerte")
plt.plot(channels, linfunc(channels, popt[0], popt[1]), "r-",
         label="linear fit: time / channel = ({0} $\pm$ {1}) ns\ntime(#channel=0) = ({2} $\pm$ {3}) ns".format(
                np.round(popt[0]*1e3,3),np.round(np.sqrt(pcov[0,0])*1e3,3),
                np.round(popt[1]*1e3,3), np.round(np.sqrt(pcov[1,1])*1e3,3)))
plt.xlabel("channel #")
plt.ylabel("time (ns)")
plt.legend(loc="best")
plt.savefig("zeitkalibrierung.pdf")

print "m: {0}, merr: {1}".format(popt[0], np.sqrt(pcov[0,0]))
print "b: {0}, berr: {1}".format(popt[1], np.sqrt(pcov[1,1]))

plt.show()
