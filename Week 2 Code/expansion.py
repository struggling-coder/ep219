import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import math

# Define data path and initialize variables
DATA = './linearexpansion.csv'
data = {}; num = 0; den = 0.0

# Define mean function
def _mean(l):
	return sum(l) / len(l)

# Load data
for e in file.read(open(DATA)).split('\r\n'):
	d = e.split(",")
	data[float(d[0])] = float(d[1])
	plt.scatter(float(d[0]), float(d[1]), s=1)

# Calculate best fit line
# Slope of best fit line is given by:
# slope = sum of ((xi - xm) * (yi - ym)) / ((xi - xm) ** 2) over all i
xm = _mean(data.keys()); ym = _mean(data.values())
for w in data:
	num += (w - xm) * (data[w] - ym)
	den += (w - xm) ** 2
slope = num / den; intercept = ym - slope * xm
best_fit_error = 0
for w in data:
	best_fit_error += (data[w] - (slope * w + intercept)) ** 2 # calculate the best fit error
best_fit_error = math.sqrt(best_fit_error / len(data))
print "Best estimate for length of the rod at 0 degrees Celsius is %5.2f mm" %(intercept)
print "Coefficient of linear expansion is %5.2f mm/K" %(slope)
print "Error on prediction: %5.2f mm" %(best_fit_error)

# Plot best-fit line
x = np.linspace(0, 15, 300)
plt.plot(x, slope * x + intercept, label="Coefficient of expansion = "+str(slope))

# Show plot and prediction
p_length = slope * 15 + intercept
plt.xlabel("Temperatute in Celsius")
plt.ylabel("Length in mm")
plt.scatter(15.0, p_length, s=16)
plt.figtext(0.78, .82, '$(15, %5.2f)$' %(p_length), fontsize=14, horizontalalignment='center',verticalalignment='center')

plt.show()
