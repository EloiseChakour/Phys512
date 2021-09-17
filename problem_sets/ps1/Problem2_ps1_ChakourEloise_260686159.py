# -*- coding: utf-8 -*-
"""
@author: elois
"""

import numpy as np



epsilon = 10**(-16)
sqrtEps = np.sqrt(epsilon)
x = 1.0


def x4(x):
    return x**4
    
func = np.exp

#Take a first estimate for the first derivative using an arbitrary dx value
def estimateFirstDer(fun, x, stepEst):
    newX = x + stepEst
    stepEst = newX- x
    firstDer = (fun(x+stepEst) - fun(x-stepEst))/(2*stepEst)
    return firstDer

def estimateSecondDer(fun, x, stepEst):
    newX = x + stepEst
    stepEst = newX-x
    secondDer = (fun(x + 2*stepEst) + fun(x - 2*stepEst) - 2*fun(x) )/(4*stepEst**2)
    return secondDer

def estimateThirdDer(fun, x, stepEst):
    newX = x + stepEst
    stepEst = newX-x
    stepEst = np.sqrt(stepEst)
    thirdDer = (fun(x + 3*stepEst) - 3*fun(x + stepEst) + 3* fun(x - stepEst) - fun(x - 3*stepEst))/(8*stepEst**3)
    return thirdDer

def newStepEst(fun, x, epsilon):
    first = fun(x)
    third = estimateThirdDer(fun, x, np.sqrt(epsilon))
    newStep = (epsilon*(first)/ third)**(1.0/3.0)
    return newStep


def ndiff(fun, x, epsilon, full=False):
    dxInitialGuess = np.sqrt(epsilon)
    dxNewEstimate = newStepEst(fun, x, dxInitialGuess)
    if full == False:
        return estimateFirstDer(fun, x, dxNewEstimate)
    elif full == True:
        firstDerFull = lambda x : estimateFirstDer(fun, x, dxNewEstimate)
        error = 0
        return firstDerFull, dxNewEstimate, error
    
    
numDer = ndiff(func, x, epsilon, full=False)
print(numDer)


first, dx, error = ndiff(func, x, epsilon, full=True)
print(first(1))
print(dx)
print(error)






