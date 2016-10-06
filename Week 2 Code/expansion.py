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
xm = _mean(data.keys()); ym = _mean(data.values())
for w in data:
	num += (w - xm) * (data[w] - ym)
	den += (w - xm) ** 2
slope = num / den; intercept = ym - slope * xm

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
