#task 2

from Task1_defs import q1
import numpy as np
from Task1_defs import l1,l2, x, y, q1, q2

Fx =10;
Fy = 10;

# defining funcitions for torques using the equation 3
def tau_1(Fx,Fy):
    tau1 = -Fx*l1*np.sin(q1) + Fy*l1*np.cos(q1)
    return(tau1)

def tau_2(Fx,Fy):
    tau2 = -Fx*l2*np.sin(q2) + Fy*l2*np.cos(q2)
    return(tau2)

#print("tau1",tau_1(Fx,Fy),"tau2",tau_2(Fx,Fy))

tau1 = tau_1(Fx, Fy)
tau2 = tau_2(Fx, Fy)
