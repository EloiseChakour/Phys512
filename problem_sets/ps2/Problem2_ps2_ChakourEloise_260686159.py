# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:21:28 2021

@author: elois
"""


import numpy as np
import sys

def integrate_adaptive(fun, a, b, tol, extra = None):
    #print("Integrating between", a, b)
    
    if type(extra) != np.ndarray:
        old_error = 0
        counter = 0
        failed_iterations = 0
    else:
        old_error = extra[0]
        counter = extra[1]
        failed_iterations = extra[2]

        
    
    x = np.linspace(a, b, 5)
    y = fun(x)
    dx = (x[1]-x[0])/(len(x))
    
    coarse_area = 2*dx*(y[0]+4*y[2]+y[4])/3
    fine_area = dx*(y[0]+4*y[1]+2*y[2]+4*y[3]+y[4])/3

    
    error = np.abs(coarse_area-fine_area)
    total_area = fine_area
    
    counter += 1



    


    #Return appropriate 
    if error <= tol: 
        #Return the result of the integration if the error is smaller than the tolerance
        return total_area, error, failed_iterations
    elif np.abs(error-old_error) <= 10**-14 :
        #Check to see if the error was appreciably changed by the last iteration and if the counter exists.
        if failed_iterations >= 3:
            #If there have been at least 3 iterations that have not changed the error, quit and send an error message
            sys.exit("There have been %s failed iterations. The current area is %d and the current error is %f." %(counter, total_area, error))
        else:
            #If there have not been 3 failed iterations, add 1 to the failed iteration counter
            failed_iterations += 1
            #Do another integration loop but cut in half
            info = np.zeros(3)
            info[0] = error
            info[1] = counter
            info[2] = failed_iterations
            new_x = (a+b)/2.0
            area1, error1, failed_iterations1 = integrate_adaptive(fun, a, new_x, tol/2, info)
            area2, error2, failed_iterations2 = integrate_adaptive(fun, new_x, b, tol/2, info)
            total_area += area1 + area2
            error=error1 + error2
            failed_iterations = failed_iterations1 + failed_iterations2
            return total_area, error, failed_iterations
    else:
        #If there have not been more than 3 failed iterations and the error is not within tolerance, record and return the relevant information for a new iteration
        info = np.zeros(3)
        info[0] = error
        info[1] = counter
        info[2] = failed_iterations
        #Do another integration loop but cut in half
        new_x = (a+b)/2.0
        area1, error1, failed_iterations1 = integrate_adaptive(fun, a, new_x, tol/2, info)
        area2, error2, failed_iterations2 = integrate_adaptive(fun, new_x, b, tol/2, info)
        total_area += area1 + area2
        error=error1+error2
        failed_iterations = failed_iterations1 + failed_iterations2
        return total_area, error, failed_iterations


#Some Tester Functions I used
def lorentz(x):
    lor = 1.0/(1.0 + x**2)
    return lor

def linear(x):
    return x

# Testing parameters
fun = np.sin
a = 0
b = np.pi
tol = 1e-7

#Compute the integral
area, error, failed_iterations = integrate_adaptive(fun, a, b, tol)

#Print the results
print("The area is", area)
print("The error is", error)
print("The number of failed iterations was", failed_iterations)













