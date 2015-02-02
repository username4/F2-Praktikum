#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

# units and natural constants
K = 1
G = 1.0e-4
V = 1

# experimental constants
T = 120*K

# measurmetns
Bexts = np.array([0., 5., 15.,10.,0],dtype=float)*G
Us = np.array([0., 2.015, 3.404,-0.013,0],dtype=float)*V
Bs = 18.*Us-0.3  # with calibration

plt.figure(1)
plt.plot(Bexts,Us, "b-")  # linien
plt.plot(Bexts,Us, "ro")  # punkte
plt.title("Neukurve von Tb bei 120 Kelvin")
plt.xlabel("Magnetfeld zur Magnetisierung der Probe B (Tesla)")
plt.ylabel("Gemessene Spannung der SQUID U (V)")
plt.grid()
plt.savefig("neukurve.pdf")
plt.show()

