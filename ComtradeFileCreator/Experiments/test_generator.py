# Внутреннее КЗ
import cmath as m
import numpy as np
import csv


def seq_to_ph(ia, ib, ic):
    a = m.exp(1j*2*m.pi/3) # rotating multiplier
    s = np.array([[1,1,1],[a**2, a,1],[a,a**2,1]]) #the method of symmetric components for A,B,C phases
    v = np.array([ia,ib,ic])
    return tuple(np.dot(s,v))

def instanst_value(value, time, omega):
    return float(np.real(abs(value*m.sqrt(2))*m.sin(omega*time + np.angle(value))))

def add_to_dat(i, t, cmtrd, new_line):
    for j in range(len(new_line)):
        new_line[j] = np.round(new_line[j]*1000).astype('int')
    cmtrd.append ([i+1, round(t*1e6)] + new_line)

td = 250e-6
w = 100*m.pi
cmtrd = list()

# mode_1
U = 57.7*m.exp(1j*np.radians(0))
I = 1

cIa, cIb, cIc = seq_to_ph(I, 0, 0)
cUa, cUb, cUc = seq_to_ph(U, 0, 0)

t_global = -td
i_global = -1

for i in range(0,400):
    t_global += td
    i_global +=1
    add_to_dat(i_global, t_global, cmtrd, [0]*11)

apv1 = 1
apv2 = 1
apv_mode = 1

for i in range(0,4000):
    rpv = 1
    rpo = 0
    t_global += td
    i_global +=1
    t = td*i
    
    ua = instanst_value(cUa,t_global,w)
    ub = instanst_value(cUb,t_global,w)
    uc = instanst_value(cUc,t_global,w)

    ia = instanst_value(cIa,t_global,w)
    ib = instanst_value(cIb,t_global,w)
    ic = instanst_value(cIc,t_global,w)

    new_line = [ua, ub, uc]
    new_line += [ia, ib, ic]
    new_line += [rpv, rpo, apv1, apv2, apv_mode]
    add_to_dat(i_global, t_global, cmtrd, new_line)

# mode_2
U = 57.7*m.exp(1j*np.radians(0))
I = 5
cIa, cIb, cIc = seq_to_ph(I, 0, 0)
for i in range(0,200):
    rpv = 1
    rpo = 0
    kcc = 0
    t_global += td
    i_global +=1
    t = td*i
    
    ua = instanst_value(cUa,t_global,w)
    ub = instanst_value(cUb,t_global,w)
    uc = instanst_value(cUc,t_global,w)

    ia = instanst_value(cIa,t_global,w)
    ib = instanst_value(cIb,t_global,w)
    ic = instanst_value(cIc,t_global,w)

    new_line = [ua, ub, uc]
    new_line += [ia, ib, ic]
    new_line += [rpv, rpo, apv1, apv2, apv_mode]
    add_to_dat(i_global, t_global, cmtrd, new_line)

# mode_3
U = 57.7*m.exp(1j*np.radians(0))
I = 0
cIa, cIb, cIc = seq_to_ph(I, 0, 0)
for i in range(0,4000):
    rpv = 0
    rpo = 1
    kcc = 0
    t_global += td
    i_global +=1
    t = td*i
    
    ua = instanst_value(cUa,t_global,w)
    ub = instanst_value(cUb,t_global,w)
    uc = instanst_value(cUc,t_global,w)

    ia = instanst_value(cIa,t_global,w)
    ib = instanst_value(cIb,t_global,w)
    ic = instanst_value(cIc,t_global,w)


    new_line = [ua, ub, uc]
    new_line += [ia, ib, ic]
    new_line += [rpv, rpo, apv1, apv2, apv_mode]
    add_to_dat(i_global, t_global, cmtrd, new_line)

# mode_4
I = 5
cIa, cIb, cIc = seq_to_ph(I, 0, 0)
for i in range(0,200):
    rpv = 1
    rpo = 0
    kcc = 1
    t_global += td
    i_global +=1
    t = td*i
    
    ua = instanst_value(cUa,t_global,w)
    ub = instanst_value(cUb,t_global,w)
    uc = instanst_value(cUc,t_global,w)

    ia = instanst_value(cIa,t_global,w)
    ib = instanst_value(cIb,t_global,w)
    ic = instanst_value(cIc,t_global,w)

    new_line = [ua, ub, uc]
    new_line += [ia, ib, ic]
    new_line += [rpv, rpo, apv1, apv2, apv_mode]
    add_to_dat(i_global, t_global, cmtrd, new_line)

# mode_5
I = 0
cIa, cIb, cIc = seq_to_ph(I, 0, 0)
for i in range(0,6000):
    rpv = 0
    rpo = 1
    kcc = 1
    t_global += td
    i_global +=1
    t = td*i
    
    ua = instanst_value(cUa,t_global,w)
    ub = instanst_value(cUb,t_global,w)
    uc = instanst_value(cUc,t_global,w)

    ia = instanst_value(cIa,t_global,w)
    ib = instanst_value(cIb,t_global,w)
    ic = instanst_value(cIc,t_global,w)

    new_line = [ua, ub, uc]
    new_line += [ia, ib, ic]
    new_line += [rpv, rpo, apv1, apv2, apv_mode]


    add_to_dat(i_global, t_global, cmtrd, new_line)

# mode_6
I = 0
cIa, cIb, cIc = seq_to_ph(I, 0, 0)
for i in range(0,200):
    rpv = 0
    rpo = 1
    kcc = 1
    t_global += td
    i_global +=1
    t = td*i
    
    ua = instanst_value(cUa,t_global,w)
    ub = instanst_value(cUb,t_global,w)
    uc = instanst_value(cUc,t_global,w)

    ia = instanst_value(cIa,t_global,w)
    ib = instanst_value(cIb,t_global,w)
    ic = instanst_value(cIc,t_global,w)

    new_line = [ua, ub, uc]
    new_line += [ia, ib, ic]
    new_line += [rpv, rpo, apv1, apv2, apv_mode]
    add_to_dat(i_global, t_global, cmtrd, new_line)

# mode_7
U = 57.7*m.exp(1j*np.radians(0))
I = 0
cIa, cIb, cIc = seq_to_ph(I, 0, 0)
for i in range(0,4000):
    rpv = 0
    rpo = 1
    kcc = 0
    t_global += td
    i_global +=1
    t = td*i
    
    ua = instanst_value(cUa,t_global,w)
    ub = instanst_value(cUb,t_global,w)
    uc = instanst_value(cUc,t_global,w)

    ia = instanst_value(cIa,t_global,w)
    ib = instanst_value(cIb,t_global,w)
    ic = instanst_value(cIc,t_global,w)


    new_line = [ua, ub, uc]
    new_line += [ia, ib, ic]
    new_line += [rpv, rpo, apv1, apv2, apv_mode]

    add_to_dat(i_global, t_global, cmtrd, new_line)


with open("comtrade2.dat", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(cmtrd)
    