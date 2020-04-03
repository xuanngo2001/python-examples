#!/usr/bin/python3
import matplotlib
matplotlib.use('Agg')
 
import numpy as np 
from scipy.stats import linregress
import matplotlib.pyplot as plt 
 
# Your data points.
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]) 
 
# Get slope, intercept from linregress() to plot y' = intercept + slope*x
(slope, intercept, rvalue, pvalue, stderr) = linregress(x,y)
 
# Plot data points
plt.scatter(x,y, color="red", marker="o", label="Original data")
 
 
# Plot linear regression line.
y_pred = intercept + slope*x
plt.plot(x,y_pred, color="green", label="Fitted line")
 
# Set labels
plt.legend(loc='best')
plt.xlabel('x') 
plt.ylabel('y') 
 
# Save result in file.
plt.savefig("scipy-linregress.png")