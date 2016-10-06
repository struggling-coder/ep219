import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

# Plotting the contours
x1, y1 = np.mgrid[-6:6:.01, -6:6:.01] 
pos = np.empty(x1.shape + (2,))
pos[:, :, 0] = x1
pos[:, :, 1] = y1
rv1 = multivariate_normal([0, 0], [[9.0, -2.0], [-2.0, 6.0]]) 
# The first argument is the mean and second is the covariance matrix
plt.axis('equal')
plt.contour(x1, y1, rv1.pdf(pos)) # Creates contour plot

# Generating random samples
x, y = multivariate_normal.rvs([0, 0], [[9.0, -2.0], [-2.0, 6.0]], 4000000).T

# Plotting Histogram
xedges = np.arange(-6.0, 6.06, 0.06) # x-coordinate of edges of  bins
yedges = np.arange(-6.0, 6.06, 0.06) # y- coordinate of edges of bins
H, xedges, yedges = np.histogram2d(y, x, bins=(xedges, yedges))
fig = plt.figure(figsize=(14, 14))
ax1 = fig.add_subplot(221)
ax1.set_title('2D Histogram')
X, Y = np.meshgrid(xedges, yedges)
ax1.pcolormesh(X, Y, H) # 2D histogram with red colour for larger numbers and blue for smaller
ax1.set_aspect('equal')

# Calculating z
z = (6*x**2 + 4*x*y + 9*y**2)/50
ax2 = fig.add_subplot(223)
ax2.hist(z, 100, (0, 15.0)) # 100 bins for z between 0 and 15
mean_obs = sum(z)/len(z) # Observed Mean
sd_obs = (sum((z-mean_obs)**2)/(len(z)-1))**0.5 # Observed standard deviation
print('The way it is written, z is chi-square distributed with f=2,\nwhich is an exponential distribution as can be seen in the histogram.')
print('Estimate of mean: %f , Expected mean: 2.0' %(mean_obs))
print('Estimate of standard deviation: %f, Expected standard deviation: 2.0' %(sd_obs))