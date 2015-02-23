#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

# units and natural constants
K = 1
G = 1.0e-4
Tesla = 1.0
milli = 1.0e-3
V = 1

# experimental constants
T = 120*K

# measurmetns
# Bexts = np.array([0., 5., 15.,10.,0],dtype=float)*milli*Tesla
Bexts = np.array([0., 5., 10, 15],dtype=float)*milli*Tesla

# Us = np.array([0., 2.015, 3.404,-0.013,0],dtype=float)*V
Us = np.array([0., 2.015, -0.013, 3.404],dtype=float)*V
Bs = 18.*Us-0.3  # with calibration

plt.figure(1)
plt.plot(Bexts,Bs, "b--")  # linien
plt.plot(Bexts,Bs, "ro")  # punkte
plt.title("Neukurve von Tb bei 120 Kelvin")
plt.xlabel("Magnetfeld zur Magnetisierung der Probe B (T)")
plt.ylabel("Magnetfeld der SQUID B (T)")
plt.grid()
plt.savefig("neukurve.pdf")
plt.show()

