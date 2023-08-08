import numpy as np
import cmath as m

"""formation of phase signals by the method of symmetric components"""
def seq_to_ph(i1, i2, i3):
    a = m.exp(1j*2*m.pi/3)
    s = np.array([[1,1,1],[a**2, a,1],[a,a**2,1]])
    v = np.array([i1,i2,i3])
    return tuple(np.dot(s,v))

"""Generation of instant signal values"""
def instanst_value(value, time, omega):
    return float(np.real(abs(value*m.sqrt(2))*m.sin(omega*time + np.angle(value))))

"""Adding parameters to the .dat file"""
def add_to_dat(i, t, cmtrd, new_line):
    for j in range(len(new_line)):
        new_line[j] = np.round(new_line[j]*1000).astype('int')
    cmtrd.append ([i+1, round(t*1e6)] + new_line)
    
