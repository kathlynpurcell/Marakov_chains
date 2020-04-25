# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 20:04:32 2020

@author: "kpurc
"""

###chance of gambler's ruin for flipping a coin once a turn

import numpy as np
import pandas as pd
#from random import seed
import numpy.random
import matplotlib.pyplot as plt
lst = []
x = []

p = 18/37
pl = 19/37
d0 = 20 #dollars initial
g = 10 #dollars gambling
M = np.array([[1, pl, 0, 0, 0],
              [0, 0, pl, 0, 0],
              [0, p, 0, pl, 0],
              [0, 0, p  , 0, 0],
              [0, 0, 0, p  , 1]])

s0 = np.array ([[0],
                [0],
                [1],
                [0],
                [0]])

ivl = 1
state = 2
d=d0
#print("Money:", d0)
number =0

while ivl < 100:
    number=number+1
    sN = np.dot(M,s0)

    r1=np.random.rand()
    if r1 < p:
        state = state+1
        d=d+g
        print("Gained $", g, "Money:", d)
    if r1 > p:
        state = state-1
        d=d-g
        print("Lost $", g, "Money:", d)
    
    plt.scatter(ivl, d, label=number)
    
    if state == 0:
        print(0)
        lst.append(0)
        #print("Lost all your money", "Money:", d)
        break
        
    if state == 4:
        #print("Won $", g, ", Walk away", "Money:", d)
        print(1)
        lst.append(1)
        break
       

    
    s0=sN
    ivl=ivl+1 



#plt.hist(lst, bins=100)
#plt.plot()
plt.title("Gambler's Ruin Roulette Init Pocket: "+str(d0)+" p: "+str(p))
#plt.title("Gambler's Ruin Init Savings:"+str(d0)+" Bet:"+str(g)+" P:"+str(p))

#plt.legend(loc="lower center",fontsize=14)
plt.xlabel("Times")
plt.ylabel("Money in Pocket")
plt.show()
#plt.savefig("Lotka-Voltera_Phase_int_R="+str(R)+"F="+str(F)+".png")

