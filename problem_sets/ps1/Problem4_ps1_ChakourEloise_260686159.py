# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 17:03:16 2021

@author: elois
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate 

#Define a function that returns the value of a lorentzian function at any x point or an array of x points
def lorentz(x):
    yval = 1.0/(1.0 + x**2)
    return yval

#Do a third order polynomial interpolation with no splines
#Inputs: an an array of x points and the function to interpolate. 
#Outputs: an array of the x values and an array of interpolated values of the function at these points
def polyCubic(x,fun):
    #Define the array of x values for which it will interpolate
    xInterp = np.delete(x, [0])
    xInterp = np.delete(xInterp, [len(xInterp)-2, len(xInterp)-1])
    #Initiate an array to store the interpolated values
    interpolatedFctVal = np.zeros(len(x)-3)
    #Fit the polynomial 
    coeffs = np.array(np.polynomial.polynomial.polyfit(xInterp, fun(xInterp), 3))
    for i in range(1, len(x)-2):
        #Evaluate the polynomial
        polynomialFit = coeffs[0] + coeffs[1]*x[i] + coeffs[2]*x[i]**2 + coeffs[3]*x[i]**3
        #Store the interpolated value
        interpolatedFctVal[i-1]= polynomialFit
    return interpolatedFctVal, xInterp


#Do a third order polynomial interpolation with splines
#Inputs: an an array of x points and the function to interpolate. 
#Outputs: an array of the x values and an array of interpolated values of the function at these points
def cubicSplines(x, fun):
    xInterp = np.linspace(-1, 1, len(x))
    #Find the y values between which we want to interpolate 
    yInterp = fun(x)
    #Set up spline interpolation
    spline = interpolate.splrep(x, yInterp)
    interpolatedFctVal = interpolate.splev(xInterp, spline)
    return interpolatedFctVal, xInterp


def rational(x, fun):
    #stub
    return


def residuals(fun, interp, x):
    interpVals, xInterp = interp(x, fun)
    trueVals = fun(xInterp)
    difference = []
    for i in range(len(xInterp)):
        diff = abs(trueVals[i]-interpVals[i])
        difference.append(diff)
    return difference












#Defines the variables we will need to feed into the functions
numPts = 100
xval_trig = np.linspace(-np.pi/2.0, np.pi/2, numPts)
xval_lor = np.linspace(-1.0, 1.0, numPts)
cos = np.cos(xval_trig)
lor = lorentz(xval_lor)

#Do the interpolation for the cubic polynomial with no splines on both a Cos and a Lorentzian Fct
cosine,xInterp = polyCubic(xval_trig, np.cos)
difference1 = residuals(np.cos, polyCubic, xval_trig)

LOR, xInterp2 = polyCubic(xval_lor, lorentz)
difference2 = residuals(lorentz, polyCubic, xval_lor)


#Plot the original cosine function, the interpolation and the difference
plt.figure(num=1, figsize=(8,4))
plt.plot(xval_trig, cos)
plt.plot(xInterp, cosine)
plt.plot(xInterp, difference1)



#Plot the original lorentzian function, the interpolation and the difference
plt.figure(num=3, figsize=(8,4))
plt.plot(xval_lor, lor)
plt.plot(xInterp2, LOR)
plt.plot(xInterp2, difference2)


#Do the interpolation for the cubic polynomial with splines on both a Cos and a Lorentzian Fct
cosSpl, xInterpSpl1= cubicSplines(xval_trig, np.cos)
differenceSplineCos = residuals(np.cos, cubicSplines, xval_trig)


lorSpl, xInterpSpl2 = cubicSplines(xval_lor, lorentz)
differenceSplineLor = residuals(lorentz, cubicSplines, xval_lor)


#Plot the original cosine function
plt.figure(num=4, figsize=(8,4))
plt.plot(xval_trig, cos)
plt.plot(xInterpSpl1, cosSpl)
plt.plot(xInterpSpl1, differenceSplineCos)



#Plot the original lorentzian function
plt.figure(num=5, figsize=(8,4))
plt.plot(xval_lor, lor)
plt.plot(xInterpSpl2, lorSpl)
plt.plot(xInterpSpl2, differenceSplineLor)


plt.figure(num=7, figsize=(8,4))
plt.plot(xInterp, difference1)
plt.plot(xInterpSpl1, differenceSplineCos)



















