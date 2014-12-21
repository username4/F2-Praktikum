#!/usr/bin/python2
import numpy as np, matplotlib.pyplot as plt
import scipy.optimize as opt 

def gaus(x, mu, norm, sigma):
    return  norm * 1./np.sqrt(2*np.pi*sigma**2) * np.exp(-1/2*(x-mu)**2/sigma**2)


# plotte histogramm
data = np.loadtxt("mehrkanal.DAT")
hist, bins = np.histogram(data, bins=200, range = [data.min(),data.max()-1] )


fitbins1 = bins[(bins>10)*(bins<22)]
fithist1 = hist[(bins>10)*(bins<22)]


fitbins2 = bins[(bins>22)*(bins<26)]
fithist2 = hist[(bins>22)*(bins<26)]

p01 = [15., 800., 5.]
p02 = [23., 100., 1.]

popt1, pcov1 = opt.curve_fit(gaus, fitbins1, fithist1, p0=p01)
popt2, pcov2 = opt.curve_fit(gaus, fitbins2, fithist2, p0=p02)

plt.figure()
plt.plot(fitbins1, gaus(fitbins1, popt1[0], popt1[1], popt1[2]), linewidth=1.5,
         label="mean: (" + str(np.round(popt1[0],3))+r"$\pm$ "+str(np.round(pcov1[0,0],2))+") pA")
plt.plot(fitbins2, gaus(fitbins2, popt2[0], popt2[1], popt2[2]), "r", linewidth=1.5,
         label= "mean: (" + str(np.round(popt2[0],3))+r"$\pm$ "+str(np.round(pcov2[0,0],2)) +") pA")

plt.legend(loc="best")
# zeichne histogramm 

plt.grid()
plt.xlabel(r"Strom (pA)")
plt.ylabel(r"counts")

plt.step(bins,np.append(hist,hist[-1]), # plt.step benoetigt als argumente linke und rechte bingrenzen und deren hoehen 
            where="post", # bins sind immer nach dem angegebenen x-wert 
            color="#000000") 
plt.savefig("mehrkanal_histo.pdf") # plots besser als vektorgrafik speichern, also pdf oder 

plt.show()
