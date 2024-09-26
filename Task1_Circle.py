#import all the required libraries and modules
import numpy as np
from Task1_defs import q_1 ,q_2, r,l1 ,l2
import matplotlib.pyplot as plt

# ite is the number of iterations
#ang is the list of angles to make a circle
ite = 50
ang = np.linspace(0, 2*np.pi, ite)
x = r*np.cos(ang)
y = r*np.sin(ang)

#q1 and q2 are a fucntions of x and y
q1 = q_1(x,y) 
q2 = q_2(x,y)

# using the for loop we can plot the position of the links at each iteration.
# which together make a animation effect
for i in range(100):
    
    l_one = (l1 * np.cos(q1[i]), l2 * np.sin(q1[i]))
    l_two =  (l_one[0]+l2 * np.cos(q2[i]),l_one[1]+l2 * np.sin(q2[i]))
     
    plt.xlim([-30, 30])
    plt.ylim([-30, 30])

    origin = (0, 0)
    plt.plot([origin[0], l_one[0]], [origin[1], l_one[1]], '-o')
    plt.plot([l_one[0],l_two[0]],[l_one[1],l_two[1]], '-o')
    plt.plot(x,y)
 

    plt.pause(0.0001)

plt.ioff()
plt.show()
