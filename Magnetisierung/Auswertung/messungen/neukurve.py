#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

# units and natural constants
K = 1
G = 1.0e-4
Tesla = 1.0
milli = 1.0e-3
micro = 1.0e-6
V = 1

# experimental constants
T = 120*K

# measurmetns

Bexts = np.array([0., 5., 10, 15], dtype=float)*milli*Tesla

#Us = np.array([0., 2.015, -0.013, 3.404],dtype=float)*V
Bs = np.array([0., 19., 27., 37.], dtype=float)*milli*Tesla
Bs180 = np.array([0., 15., 22., 29.], dtype=float)*milli*Tesla

plt.figure(1)
plt.plot(Bexts/(milli*Tesla),Bs/(milli*Tesla), "r--")  # linien
plt.plot(Bexts/(milli*Tesla),Bs/(milli*Tesla), "r^", label="$T = 120$K", markersize=8)  # punkte

plt.plot(Bexts/(milli*Tesla),Bs180/(milli*Tesla), "b--")  # linien
plt.plot(Bexts/(milli*Tesla),Bs180/(milli*Tesla), "bo", label="$T = 180$K", markersize=8)  # punkte

plt.title("Neukurven von Tb", fontsize=18)
plt.xlabel(r"Magnetfeld zur Magnetisierung: $B_{\rm extern}$ (mT)", fontsize=18)
plt.ylabel(r"Magnetfeld der Probe: $B$ (mT)", fontsize=18)
plt.legend(loc="best",numpoints=1)
plt.grid()
plt.savefig("neukurve.pdf")
plt.show()

