import cmath as m
import numpy as np
from service import seq_to_ph, instanst_value, add_to_dat
import csv

td = 250e-6
w = 100*m.pi
cmtrd = list()

# the exponential form of writing a complex number
U = 57.7*m.exp(1j*np.radians(0))
Ivn = 1*m.exp(1j*np.radians(0))
Inn = -5*m.exp(1j*np.radians(30))

# formation of the algebraic form of writing a complex number for each phase
cIavn, cIbvn, cIcvn = seq_to_ph(Ivn, 0, 0)
cIann, cIbnn, cIcnn = seq_to_ph(Inn, 0, 0)
cUa, cUb, cUc = seq_to_ph(U, 0, 0)

# Create different signals
cIavn = 1*m.exp(1j*np.radians(0))
cIbvn = 1.2*m.exp(1j*np.radians(230))
cIcvn = 0.9*m.exp(1j*np.radians(150))

cIann = -5.1*m.exp(1j*np.radians(10+30))
cIbnn = -1*m.exp(1j*np.radians(250+30))
cIcnn = -5*m.exp(1j*np.radians(105+30))

# filling the comtrade array
for i in range(0,400):
    add_to_dat(i, td*i, cmtrd, [0]*11)

for i in range(0,4000):
    di = 1
    MTZ = 0
    t = td*i
    Ua = instanst_value(cUa,t,w)
    Ub = instanst_value(cUb,t,w)
    Uc = instanst_value(cUc,t,w)

    Iavn = instanst_value(cIavn,t,w)
    Ibvn = instanst_value(cIbvn,t,w)
    Icvn = instanst_value(cIcvn,t,w)

    Iann = instanst_value(cIann,t,w)
    Ibnn = instanst_value(cIbnn,t,w)
    Icnn = instanst_value(cIcnn,t,w)

    new_line = [Ua, Ub, Uc]
    new_line += [Iavn, Ibvn, Icvn,
                 Iann, Ibnn, Icnn]
    new_line += [di, MTZ]

    add_to_dat(i, t, cmtrd, new_line)

with open("Test.dat", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(cmtrd)