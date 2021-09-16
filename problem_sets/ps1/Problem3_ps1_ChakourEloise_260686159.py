# -*- coding: utf-8 -*-
"""
@author: elois
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate 

dat=np.loadtxt('lakeshore.txt')

rng = np.random.default_rng(seed=12345)

#Should return temp and uncertainty on temp
def lakeshore(V,data):
    #Decompose the data into temp and voltage data
    temp = data[:, 0]
    volt = data[:, 1]
    #Pick a random 10% of values to use for comparison
    numTestPts = int(np.floor(0.1*len(temp)))
    #Generate the correct number of random integers
    indices = []
    for i in range(len(temp)):
        indices.append(i)
    testPts = rng.choice(indices, size=numTestPts, replace=False)
    testPts.sort
    testTemp = []
    testVolt = []
    for i in range(len(testPts)):
        index = testPts[i]
        testTemp.append(temp[index])
        testVolt.append(volt[index])
    testVolt, testTemp = zip(*sorted(zip(testVolt, testTemp)))
    
    interpTemp = [ value for value in temp if value not in testTemp]
    interpVolt = [ value for value in volt if value not in testVolt]

    interpVolt, interpTemp = zip(*sorted(zip(interpVolt, interpTemp)))

    spline = interpolate.splrep(interpVolt, interpTemp)
    T = interpolate.splev(V, spline)
    
    interpolatedTemps = interpolate.splev(testVolt, spline)
    
    deltaT = np.mean(abs(interpolatedTemps - testTemp))
    
    
    
    
    return T, deltaT






V = np.linspace(0.095, 1.600, 20)
t, dt = lakeshore(V, dat)

print(t)
print(dt)




plt.figure(num=1, figsize=(16,8))
plt.plot(dat[:, 1], dat[:, 0])
plt.plot(V, t)


















