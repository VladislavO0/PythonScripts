import numpy as np
import cmath as m

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
    