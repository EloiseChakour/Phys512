# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:22:17 2021

@author: elois
"""

import numpy as np
import sys


#This function fits a chebyshev polynomial for a log_2 between 0.5 and 1.
#Inputs: number of points to use for the Chebyshev fit (pts) and the initial guess for the order of the Chebyshev polynomial to fit (ord_Guess). 
#Outputs: The Chebyshev coefficients, the order of the polynomial and the average error found in testing with this fit (accuracy)
def evaluateCheb1(pts, ord_Guess):
    x_log = np.linspace(0.5, 1.0, pts)
    y = np.log2(x_log)
    x_cheb = x_log
    cheb = np.polynomial.chebyshev.chebfit(x_cheb,y, ord_Guess)
    
    x_test = np.linspace(0.5, 1.0, pts + 20)
    cheb_evaluated = np.polynomial.chebyshev.chebval(x_test, cheb)
    ref_vals = np.log2(x_test)
    error = np.abs(cheb_evaluated - ref_vals)
    accuracy = np.average(error)
    
    if accuracy >= 1e-6:
       ord_Guess  = ord_Guess + 1
       return evaluateCheb1(pts, ord_Guess)
    elif (accuracy <= 1e-6) and (accuracy >= 1e-7):
       return cheb, ord_Guess, accuracy
    elif accuracy < 1e-7:
        ord_Guess = ord_Guess - 1
        return evaluateCheb1(pts, ord_Guess)

#This function evaluates a Chebyshev polynomial at a certain x to extimate a log_2
#Inputs: A value of x for which to evaluate the polynomial (x), the number of points to use for the fit (pts) and the initial guess for the order of the polynomial (ord_Guess)
#Outputs: The estimated valye of log_2 at the given x and the order of the polynomial used
def mylog(x, pts, ord_Guess = 10):
    #Check to see that the value of x is valid.
    if x > 1:
        sys.exit("This is not a valid value of x. Please enter a value between 0.5 and 1.0.")
    if x< 0.5:
        sys.exit("This is not a value of x. Please enter a value between 0.5 and 1.0.")
    #Compute the coefficients for the Chebyshev Polynomial
    coeffs, order, accuracy = evaluateCheb1(pts, ord_Guess)
    value = np.polynomial.chebyshev.chebval(x, coeffs)
    return value, order


def evaluateCheb2(pts, ord_Guess):
    
    
    
    
    
    return 

def mylog2(x):
    #stub
    return



val_log2, order = mylog(0.6, 10)
print("The value obtained was", val_log2)
print("The order of the polynomial that was used was", order)


























