#!/usr/bin/python2
import numpy as np, matplotlib.pyplot as plt
import scipy.optimize as opt 


# plotte histogramm
data = np.loadtxt("mehrkanal.DAT")
hist, bins = np.histogram(data, bins=30, range = [data.min(),data.max()-1] )

# zeichne histogramm 
plt.figure(1) # sowas wie die canvas bei root
plt.grid()
plt.xlabel(r"Strom (pA)")
plt.ylabel(r"counts")

plt.bar(bins[:-1],hist, # plt.bar benoetigt nur linke bingrenzen (bins[:-1]) und deren hoehen
        width=(bins[1]-bins[0]), # nehme konstante binbreite an, dann haben alle bins die Breite vom ersten bin
        color="#FFFFFF") 

plt.figure(2)
plt.grid()
plt.xlabel(r"Strom (pA)")
plt.ylabel(r"counts")

plt.step(bins,np.append(hist,hist[-1]), # plt.step benoetigt als argumente linke und rechte bingrenzen und deren hoehen 
            where="post", # bins sind immer nach dem angegebenen x-wert 
            color="#000000") 
plt.savefig("mehrkanal_histo.pdf") # plots besser als vektorgrafik speichern, also pdf oder 

plt.show()
