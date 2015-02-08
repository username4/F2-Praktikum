#!/usr/bin/python2
import numpy as np

# Konstanten
m = 1
MeV = 1e6
GeV = 1e9
nano = 1e-9
barn = 1e-28 * m**2

# Messwerte
gamma_ll = 83.83 * MeV
gamma_had = 28 * gamma_ll

# hadronische Ereignisse bei 1000 Messwerten
# wir hatten 450 hadronische ereignisse 499 gesamtereignissen gemessen
N_had = 1000.0/499.0 * 450

L = 28.48 / (nano*barn) # Luminositaet
m_Z = 91.1876*GeV


# berechne wirkungsquerschnitt
sigma_had = (1-0.263) * N_had/L

print "Wirkungsquerschnitt in barn: ", sigma_had / barn

# gesamte Zerfallsbreite des Z_0:

gamma_tot = np.sqrt(12*np.pi*gamma_ll*gamma_had / (m_Z**2 * sigma_had))

print "Zerfallsbreite gamma_tot", gamma_tot


# berechne Anzahl der Neutrinofamilien
gamma_inv = gamma_tot - gamma_had  - 3*gamma_ll # gemessene zerfallsbreite fuer neutrinos
gamma_theo = 166.1*MeV # theoretische zerfallsbreite fuer 1 neutrinofamilie

N_nu = gamma_inv / gamma_theo
print "Anzahl der Neutrinofamilien: ", N_nu
