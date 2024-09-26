#importing required libraries
import numpy as np
from scipy.integrate import solve_ivp
from Task1_defs import l1,l2,m1,m2,g
#from task_2 import tau1, tau2

tau1 = 1
tau2 = 1

t = np.linspace(0, 1, 100)

# this solves the lagrange equations and we ger the output as w1,w2,q1,q2
# this will help in solving the task3 and task2
def dWdt(t, Wdot):
    w1, w2, q1, q2 = Wdot
    s = np.sin(q2-q1)
    c = np.cos(q2-q1)
    
    A = np.array([[1/3*m1*l1**2+m2*l1**2 , m2*l2*l1*c/2],
                   [m2*l1*l2*c/2 , 1/3*m2*l2**2+(m2*l2**2)/4]])

    C = np.array([[(m2*l1*l2*w2*(w2-w1)*s)/2-(m2*g*l1*np.cos(q2))/2-(m2*g*l1*np.cos(q2))+tau1],
                 [(m2*l1*l2*w1*(w2-w1)*s)/2-(m1*g*l2/2*np.sin(q2))+tau2]]) 

    B = np.dot(np.linalg.inv(A), C)
    
    return B
    
w1_0 = 0
w2_0 = 0
q1_0 = 0
q2_0 = 0
Wdot_0 = (w1_0, w2_0, q1_0, q2_0)

#using this module to solve the differential equations
sol = solve_ivp(dWdt, t_span=(0,max(t)), y0 = Wdot_0, t_eval= t )