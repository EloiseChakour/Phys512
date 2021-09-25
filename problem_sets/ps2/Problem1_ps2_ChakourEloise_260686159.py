# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:21:32 2021

@author: elois
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


#Computes the numerical constant in front of the integral
def computeConstant(R, s):
    e = 8.8541878128* 10**(-12)
    constant = (2*np.pi*R*R*s)/(4.0*np.pi*e)
    return constant

#Defines the part of the function we need to integrate
def toIntegrate(x, z, R):
    num = z-R*x
    denom = (R*R + z*z - 2.0*R*z*x)**(3.0/2.0)
    func = (num/denom)
    return func

#Numerically intergates the function with scipy.integrate.quad
def evalQuad(fun, z, R, s, a = -1, b = 1):
    integral, err = integrate.quad(fun, a, b, args=(z, R))
    return integral, err


#Evaluates the integral for a series of z values for the purpose of plotting
def getQuadVals(z_min, z_max, fun, R, s):
    pts = (z_max-z_min)*10 #Number of z valyes for which to evaluate the integral
    #Make sure that R is one of the points
    pts2 = int(np.floor(pts/2))
    z_arr1 = np.linspace(z_min, R, pts2)
    z_arr2 = np.linspace(R, z_max, pts2)
    z_arr = []
    for i in range(pts2):
        z_arr.append(z_arr1[i])
    for i in range(pts2):
        z_arr.append(z_arr2[i])
    const = computeConstant(R, s) #Computes the scaling constant
    int_Vals = []
    for i in range(pts):
        integral_Val, err = evalQuad(fun, z_arr[i], R, s)
        integral_Val_Scaled = const * integral_Val
        int_Vals.append(integral_Val_Scaled)
    return z_arr, int_Vals



#Inputs: The function to integrate (fun), the min and max z values to evaluate, the radius of the sphere (R) and its surface charge
#Returns the value of the numerical integral at all of the z values and said z values
#Uses the Simpson expression for around steep peaks
def myIntegrator(fun, z_min, z_max, R, s, dx = 1e-8, a = -1, b=1):
    #Define the number of points you want
    pts = (z_max-z_min)*20
    pts2 = int(np.floor(pts/2))
    #Make sure R is one of the points
    z_arr1 = np.linspace(z_min, R, pts2)
    z_arr2 = np.linspace(R, z_max, pts2)
    z_arr = []
    for i in range(pts2):
        z_arr.append(z_arr1[i])
    for i in range(pts2):
        z_arr.append(z_arr2[i])
    #Define the points for Simpson's
    x = np.linspace(-1, 1, 7)
    #Compute the scaling constnat 
    const = computeConstant(R, s)
    integral_Vals = []
    
    #Compute the numerical value for the z<R
    for i in range(pts2):
        y = toIntegrate(x, z_arr1[i], R)
        area = const*(dx*(9*y[0] + 28*y[1] + 23*y[2] + 24*y[3] + 24*y[4] + 23*y[-3] + 28*y[-2] + 9*y[-1])/24)
        integral_Vals.append(area)
    
    #Compute the numerical value for the z>R
    for i in range(pts2):
        y = toIntegrate(x, z_arr2[i], R)
        area = const*(dx*(9*y[0] + 28*y[1] + 23*y[2] + 24*y[3] + 24*y[4] + 23*y[-3] + 28*y[-2] + 9*y[-1])/24)
        integral_Vals.append(area) 
        
    return z_arr, integral_Vals
    
    
    
    
    
    
    
    







#Set Testing Variables
R = 1.0 #The Sphere's Radius
s = 1.0 #The Sphere's Surface Charge
r_min = 0
r_max = int(2*R)
    
#Compute the two integration methods
z, E = getQuadVals(r_min, r_max, toIntegrate, R, s)
my_z, my_E = myIntegrator(toIntegrate, r_min, r_max, R, s)

#Plot the Quad version
plt.figure(num=1, figsize=(4,4))
plt.title('Electrical Field Quad')
plt.axvline(x=R, color='r', linestyle=':')
plt.plot(z, E, label='Quad')
plt.xlabel("Vertical distance from the center of the sphere")
plt.ylabel("Magnitude of the electric field")
plt.legend()

#Plod my version
plt.figure(num=2, figsize=(4,4))
plt.title('Electrical Field My Integrator')
plt.plot(my_z, my_E, label='My Integrator')
plt.axvline(x=R, color='r', linestyle=':')
plt.ylim(bottom=0)
plt.xlabel("Vertical distance from the center of the sphere")
plt.ylabel("Magnitude of the electric field")
plt.legend()












