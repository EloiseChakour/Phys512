# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:22:17 2021

@author: elois
"""

import numpy as np




def mylog(pts, ord_Guess = 10):
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
       return mylog(pts, ord_Guess)
    elif (accuracy <= 1e-6) and (accuracy >= 1e-7):
       return cheb, ord_Guess, accuracy
    elif accuracy < 1e-7:
        ord_Guess = ord_Guess - 1
        return mylog(pts, ord_Guess)
    else:
        print("Hello")
        return 2





def mylog2(x):
    #stub
    return





cheb, order, accuracy =mylog(20)
print("The coefficients are", cheb)
print("The order is", order)
print("The accuracy is", accuracy)



























