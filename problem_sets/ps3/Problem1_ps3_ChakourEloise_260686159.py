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


def solution(x):
    y = (-1.0)*np.exp((-1.0)*np.arctan(-20.0))*np.exp(np.arctan(x))
    return y


#Compute one term of the rk4 integration
def rk4_step(fun, x, y, h):
    
    k1=fun(x,y)*h
    k2=h*fun(x+h/2,y+k1/2)
    k3=h*fun(x+h/2,y+k2/2)
    k4=h*fun(x+h,y+k3)
    dy=(k1+2*k2+2*k3+k4)/6
    
    return y + dy

def computeRK4(fun, x_0 = -20.0, x_f = 20.0, y_0 = -1, nb_steps = 200):
    h = (x_f-x_0)/nb_steps
    x = np.linspace(x_0, x_f, nb_steps)
    y = np.zeros(nb_steps)
    y[0] = y_0
    for i in range(nb_steps-1):
        y[i+1] = rk4_step(fun, x[i], y[i], h)
    return x, y


def rk4_stepd(fun, x, y, h):
    new_y_bigH = rk4_step(fun, x, y, h)
    smallH = h/2
    
    k1 = fun(x, y)*smallH
    k2 = smallH*fun(x+smallH/2, y+k1/2)
    k3 = smallH*fun(x+smallH/2, y+k2/2)
    k4 = smallH*fun(x+smallH, y+k3)
    dy=(k1+2*k2+2*k3+k4)/6
    newy = y + dy
    newx = x + smallH
    
    K1 = fun(newx, newy)*smallH
    K2 = smallH*fun(newx+smallH/2, newy + k1/2)
    K3 = smallH*fun(newx+smallH/2, newy+k2/2)
    K4 = smallH*fun(newx+smallH, newy+k3)
    Dy = (K1+2*K2+2*K3+K4)/6
    new_y_smallH = newy + Dy
    
    return new_y_bigH, new_y_smallH

    

def computeRK4_diff(fun, x_0 = -20.0, x_f = 20.0, y_0 = -1, nb_steps = 200):
    h = (x_f-x_0)/nb_steps
    x = np.linspace(x_0, x_f, nb_steps)
    y_bigH = np.zeros(nb_steps)
    y_smallH = np.zeros(nb_steps)
    y_bigH[0] = y_0
    y_smallH[0] = y_0
    for i in range(nb_steps-1):
        y_bigH[i+1], y_smallH[i+1] = rk4_stepd(fun, x[i], y[i], h)
    return x, y_bigH, y_smallH



#Compute the real solution
npt = 200
x_real = np.linspace(-20, 20, npt)
y_real = np.zeros(npt)
for i in range(len(x_real)):
    y_real[i] = solution(x_real[i])

plt.figure(num=0)
plt.plot(x_real, y_real)


#Compute the solution for rk4 with given parameters and a set step size
x, y = computeRK4(func)
#Compute the difference with the known solution
y_err = np.abs(y_real-y)

#Plot and save the figure for the solution
plt.figure(num=1)
plt.plot(x, y)
#plt.axvline(0, color='k')
plt.title("RK4 Solution for 200 Steps")
plt.savefig("rk4_200pts_setStep.jpg")

#Plot and save the figure for the error
plt.figure(num=2)
plt.plot(x, y_err)
#plt.axvline(0, color='k')
plt.title("RK4 Solution Error for 200 Steps")
plt.savefig("rk4_error_200pts_setStep.jpg")


#Compute the two solutions to compare
xx, y_bigH, y_smallH = computeRK4_diff(func)

#Compute the differences with the known solutions
y_bigH_err = np.abs(y_bigH - y_real)
y_smallH_err = np.abs(y_smallH-y_real)




plt.figure(num=3)
plt.plot(xx, y_bigH)
plt.title("RK4 Solution for h")
plt.savefig("rk4_bigH.jpg")

plt.figure(num=4)
plt.plot(xx, y_smallH)
plt.title("RK4 Solution with half h")
plt.savefig("rk4_smallH.jpg")

plt.figure(num=5)
plt.plot(xx, y_bigH_err, color='k', label="Error for big h")
plt.plot(xx, y_smallH_err, color='b', label="Error for half h")
plt.title("RK4 Solution for 200 Steps")
plt.legend()
plt.savefig("rk4_error_comaprison.jpg")




























