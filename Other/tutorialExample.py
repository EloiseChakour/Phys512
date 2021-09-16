# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 15:28:49 2021

@author: elois
"""

import numpy as np
import scipy.interpolate as intp
import matplotlib.pyplot as plt

#Unsing Bootstrap for interpolation

#Regular Interpolation
xs = np.linspace(0, 1, 100)
ys = np.exp(-xs)
plot_xs= np.linspace(0, 1, 1000)

interpolation = intp.CubicSpline(xs, ys)
plot_ys = interpolation(plot_xs)


plt.plot(plot_xs, plot_ys)
plt.plot(plot_xs, np.exp(-plot_xs))

#Boostrap 

rng = np.random.default_rng(seed=12345)
N_resamples = 10
N_samples = 40

errors=[]

for i in range(N_resamples):
    #Make list of all indices
    indices = list(range(xs.size))
    #Choose N_samples (40) indices of values to keep for new interpolation
    to_interp = rng.choice(indices, size=N_samples, replace=False)
    #Sort for increasing x value
    to_interp.sort()
    #Taking the indices for error checking (not chosen before)
    to_check = [i for i in indices if not (i in to_interp) ]
    #Using interpolation points to interpolate
    new_interpolation = intp.CubicSpline(xs[to_interp], ys[to_interp])
    #Generate y values to check error
    interpolated_ys = new_interpolation(xs[to_check])
    real_ys = ys[to_check]
    #Check abs values for errors
    errors.append(np.abs(interpolated_ys-real_ys))
    

error = np.mean(errors)
std = np.std(errors)

print(error)
print(std)

















