#importing all the required libraris
import numpy as np
from Task1_defs import q_1 ,q_2 ,l1 ,l2
import matplotlib.pyplot as plt

# defining the line equaation

c = 0; # its the intersept
m = 1; # slope of the line

x = np.linspace(-20/np.sqrt(2),20/np.sqrt(2),50)
y = m*x+c # line equation

q1 = q_1(x,y)
q2 = q_2(x,y)

for i in range(50):
    
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
    