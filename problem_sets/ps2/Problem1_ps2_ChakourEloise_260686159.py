# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:21:32 2021

@author: elois
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def computeConstant(R, s):
    e = 8.8541878128* 10**(-12)
    constant = (2*np.pi*R*R*s)/(4.0*np.pi*e)
    return constant

def toIntegrate(x, z, R):
    num = z-R*x
    denom = (R*R + z*z - 2.0*R*z*x)
    func = num/denom
    return func


def evalQuad(fun, z, R, s, a = -1, b = 1):
    integral = integrate.quad(fun, a, b, args=(z, R))
    return integral



def getQuadVals(z_min, z_max, fun, R, s):
    pts = (z_max-z_min)*10
    z_arr = np.linspace(z_min, z_max, pts)
    int_Vals = []
    for i in range(pts):
        integral_Val, err = evalQuad(fun, z_arr[i], R, s)
        int_Vals.append(integral_Val)
    return z_arr, int_Vals

R = 50.0
s = 2.0

z, E = getQuadVals(0, 100, toIntegrate, R, s)

plt.figure(num=1, figsize=(4,4))
plt.title('Electrical Field')
plt.axvline(x=50.0, color='r')
plt.plot(z, E, label='Quad')
plt.legend()













