# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 19:49:20 2021

@author: elois
"""

import numpy as np
from matplotlib import pyplot as plt



def func(x, y):
    val = y/(1.0 + x*x)
    return val





#Compute one term of the rk4 integration
def rk4_step(fun, x, y, h):
    
    k1=fun(x,y)*h
    k2=h*fun(x+h/2,y+k1/2)
    k3=h*fun(x+h/2,y+k2/2)
    k4=h*fun(x+h,y+k3)
    dy=(k1+2*k2+2*k3+k4)/6
    
    return y + dy



def rk4_stepd(fun, x, y, h):
    #stub
    return



def computeRK4(fun, x_0 = -20.0, x_f = 20.0, y_0 = -1, nb_steps = 200):
    h = (x_f-x_0)/nb_steps
    x = np.linspace(x_0, x_f, nb_steps)
    y = np.zeros(nb_steps)
    y[0] = y_0
    for i in range(nb_steps-1):
        y[i+1] = rk4_step(fun, x[i], y[i], h)
    return x, y
    

#Compute the solution for rk4 with given parameters and a set step size
x, y = computeRK4(func)

#Plot and save the figure
plt.figure(num=1)
plt.plot(x, y)
plt.axvline(0, color='k')
plt.title("RK4 Solution for 200 Steps")
plt.savefig("rk4_200pts_setStep.jpg")
































