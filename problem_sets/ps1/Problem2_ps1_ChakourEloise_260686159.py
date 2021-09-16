# -*- coding: utf-8 -*-
"""
@author: elois
"""

import numpy as np



epsilon = 10**(-16)
sqrtEps = np.sqrt(epsilon)
x = 1.0


def quadratic(x):
    return x**2
    
func = quadratic

#Take a first estimate for the first derivative using an arbitrary dx value
def estimateFirstDer(fun, x, stepEst):
    newX = x + stepEst
    stepEst = newX- x
    firstDer = (fun(x+stepEst) - fun(x-stepEst))/(2*stepEst)
    return firstDer

#Testting
estimate1 = estimateFirstDer(func, x, sqrtEps)
trueVal = 2*x

print("Testing First Derivative")
print(estimate1)
print(trueVal)
print(estimate1 == trueVal)





def estimateSecondDer(fun, x, stepEst):
    newX = x + stepEst
    stepEst = newX-x
    #secondDer = (estimateFirstDer(fun, x+stepEst, stepEst) - estimateFirstDer(fun, x-stepEst, stepEst))/(2*stepEst)
    secondDer = (fun(x + 2*stepEst) + fun(x - 2*stepEst) - 2*fun(x) )/(4*stepEst**2)
    return secondDer

estimate2 = estimateSecondDer(func, x, sqrtEps)

print("Testing Second Derivative")
print(estimate2)
print(2)
print(estimate2 == 2.0)


def newStepEst(fun, x, epsilon):
    newStep = np.sqrt(epsilon*(fun(x)/ estimateSecondDer(fun, x, np.sqrt(epsilon))))
    return newStep

newStep = newStepEst(func, x, epsilon)

print("This is the new dx size")
print(newStep)

newFirst = estimateFirstDer(func, 1, newStep)
print("Testing First Derivative with new Step Size")
print(newFirst)
print(trueVal)
print(newFirst == trueVal)



