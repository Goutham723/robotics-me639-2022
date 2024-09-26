#task 1

import numpy as np

# assgning all the constants which include lengths, masses.
l1 = 10; #length of link 1
l2 = 10; #length of link 2
m1 = 1   #mass of link 1
m2 = 1   #mass of link 2
r = 15;  #radius of the required circle
g = 9.81; #gravity

x = -15
y = -15

#defining functions for angles of the links with x axis

def theta(x,y):
    theta = np.arccos((x**2+y**2-l1**2-l2**2)/(2*l1*l2))
    return(theta)

def q_1(x,y):
    q1 = (np.arctan(y/x) - np.arctan(l2*np.sin(theta(x,y))/(l1+l2*np.cos(theta(x,y)))))
    return(q1)

def q_2(x,y):
    q2 = q_1(x,y) +theta(x,y)
    return(q2)

q1 = q_1(x,y)
q2 = q_2(x, y)
