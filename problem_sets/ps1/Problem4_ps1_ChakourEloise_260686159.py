# -*- coding: utf-8 -*-
"""
@author: elois
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate 

#Define a function that returns the value of a lorentzian function at any x point or an array of x points
def lorentz(x):
    yval = 1.0/(1.0 + x**2)
    return yval


def polyCubic(x, xInterp, fun):
    #Initiate an array to store the interpolated values
    interpolatedFctVal = np.zeros(len(x))
    #Fit the polynomial 
    coeffs = np.array(np.polynomial.polynomial.polyfit(xInterp, fun(x), 3))
    for i in range(len(xInterp)):
        #Evaluate the polynomial
        polynomialFit = coeffs[0] + coeffs[1]*x[i] + coeffs[2]*x[i]**2 + coeffs[3]*x[i]**3
        #Store the interpolated value
        interpolatedFctVal[i-1]= polynomialFit
    return interpolatedFctVal


def cubicSplines(x, xInterp, fun):
    #Evaluate the function we want to interpolate at some values of x
    yInterp = fun(x)
    #Set up spline interpolation
    spline = interpolate.splrep(xInterp, yInterp)
    #Evaluate the interpolation
    interpolatedFctVal = interpolate.splev(xInterp, spline)
    return interpolatedFctVal


def rational(x, xInterp, fun, n, m):
    matrix = np.zeros([n+m-1, n+m-1])
    y = fun(x)
    #Fit the rational function
    for i in range(n):
        matrix[:, i] = x**i
    for i in range(1, m):
        matrix[:,i-1+n]=-y*x**i
    coeffs=np.dot(np.linalg.inv(matrix),y)
    p=coeffs[:n]
    q=coeffs[n:]
    #Evaluate the rational function
    numerator=0
    for i in range(len(p)):
        numerator=numerator+p[i]*x**i
    denom=1
    for i in range(len(q)):
        denom=denom+q[i]*x**(i+1)
    #Compute the interpolated values
    interpolatedFctVal = numerator/denom  
    return interpolatedFctVal


def residuals(fun, interp, x, xInterp):
    interpVals = interp(x, xInterp, fun)
    trueVals = fun(xInterp)
    difference = []
    for i in range(len(xInterp)):
        diff = abs(trueVals[i]-interpVals[i])
        difference.append(diff)
    return difference


def residualsRat(fun, interp, x, xInterp, n, m):
    interpVals = interp(x, xInterp, fun, n, m)
    trueVals = fun(xInterp)
    difference = []
    for i in range(len(xInterp)):
        diff = abs(trueVals[i]-interpVals[i])
        difference.append(diff)
    return difference



#Defines the variables we will need to feed into the functions
numPts = 200

xval_trig = np.linspace(-np.pi/2.0, np.pi/2, numPts)
xval_trig_Interp = np.linspace(xval_trig[1], xval_trig[-1], numPts)

xval_lor = np.linspace(-1.0, 1.0, numPts)
xval_lor_Interp = np.linspace(xval_lor[1], xval_lor[-1], numPts)

cos = np.cos(xval_trig)
lor = lorentz(xval_lor)

#Do the interpolation for the cubic polynomial with no splines on both a Cos and a Lorentzian Fct
cosine = polyCubic(xval_trig, xval_trig_Interp, np.cos)
difference1 = residuals(np.cos, polyCubic, xval_trig, xval_trig_Interp)

Lor = polyCubic(xval_lor, xval_lor_Interp, lorentz)
difference2 = residuals(lorentz, polyCubic, xval_lor, xval_lor_Interp)


#Plot the original cosine function, the interpolation and the difference
plt.figure(num=1, figsize=(8,4))
plt.title('Cosine Polynomial')
plt.plot(xval_trig, cos, label='True Cos')
plt.plot(xval_trig_Interp, cosine, label='Cosine Interpolated')
plt.plot(xval_trig_Interp, difference1, label='Difference')
plt.legend()



#Plot the original lorentzian function, the interpolation and the difference
plt.figure(num=2, figsize=(8,4))
plt.title('Lorentzian Polynomial')
plt.plot(xval_lor, lor, label='True Lorentzian')
plt.plot(xval_lor_Interp, Lor, label='Lorentzian Interpolated')
plt.plot(xval_lor_Interp, difference2, label='Difference')
plt.legend()


#Do the interpolation for the cubic polynomial with splines on both a Cos and a Lorentzian Fct
cosineSpl = cubicSplines(xval_trig, xval_trig_Interp, np.cos)
differenceSpl1 = residuals(np.cos, cubicSplines, xval_trig, xval_trig_Interp)

LorSpl = cubicSplines(xval_lor, xval_lor_Interp, lorentz)
differenceSpl2 = residuals(lorentz, cubicSplines, xval_lor, xval_lor_Interp)

#Plot the original cosine function, the interpolation and the difference
plt.figure(num=3, figsize=(8,4))
plt.title('Cosine Cubic Spline')
plt.plot(xval_trig, cos, label='True Cos')
plt.plot(xval_trig_Interp, cosineSpl, label='Cosine Interpolated')
plt.plot(xval_trig_Interp, differenceSpl1, label='Difference')
plt.legend()


#Plot the original lorentzian function, the interpolation and the difference
plt.figure(num=4, figsize=(8,4))
plt.title('Lorentzian Cubic Spline')
plt.plot(xval_lor, lor, label='True Lorentzian')
plt.plot(xval_lor_Interp, LorSpl, label='Lorentzian Interpolated')
plt.plot(xval_lor_Interp, differenceSpl2, label='Difference')
plt.legend()


#Define some rational function specific variables
n = 21
m = numPts - n +1

#Do the interpolation with a rational function
cosineRat = rational(xval_trig, xval_trig_Interp, np.cos, n, m)
differenceRat1 = residualsRat(np.cos, rational, xval_trig, xval_trig_Interp, n, m)

lorRat = rational(xval_lor, xval_lor_Interp, lorentz, n, m)
differenceRat2 = residualsRat(lorentz, rational, xval_lor, xval_lor_Interp, n, m)



#Plot the original lorentzian function, the interpolation and the difference
plt.figure(num=5, figsize=(8,4))
plt.title('Cosine Rational')
plt.plot(xval_trig, cos, label='True Cos')
plt.plot(xval_trig_Interp, cosineRat, label='Cosine Interpolated')
plt.plot(xval_trig_Interp, differenceRat1, label='Difference')
plt.legend()

#Plot the original lorentzian function, the interpolation and the difference
plt.figure(num=6, figsize=(8,4))
plt.title('Lorentzian Rational')
plt.plot(xval_lor, lor, label='True Lorentzian')
plt.plot(xval_lor_Interp, lorRat, label='Lorentzian Interpolated')
plt.plot(xval_lor_Interp, differenceRat2, label='Difference')
plt.legend()



#Plot the differences from each interpolation scheme on the same graph
#Cosine
plt.figure(num=10, figsize=(8,4))
plt.title('Cosine Differences')
plt.plot(xval_trig_Interp, difference1, label='Polynomial')
plt.plot(xval_trig_Interp, differenceSpl1, label='Splines')
plt.plot(xval_trig_Interp, differenceRat1, label='Rational')
plt.legend()


#Lorentzian
plt.figure(num=11, figsize=(8,4))
plt.title('Lorentzian Differences')
plt.plot(xval_lor_Interp, difference2, label='Polynomial')
plt.plot(xval_lor_Interp, differenceSpl2, label='Splines')
plt.plot(xval_lor_Interp, differenceRat2, label='Rational')
plt.legend()
































