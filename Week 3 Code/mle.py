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

def f(data,m,c):
	val = 0
	for x in data:
		val += (data[x] - (m * x + c)) ** 2
	return val;

# Load data
for e in file.read(open(DATA)).split('\r\n'):
	d = e.split(",")
	data[float(d[0])] = float(d[1])

# Calculate best fit line
# Slope of best fit line is given by:
# slope = sum of ((xi - xm) * (yi - ym)) / ((xi - xm) ** 2) over all i
xm = _mean(data.keys()); ym = _mean(data.values())
for w in data:
	num += (w - xm) * (data[w] - ym)
	den += (w - xm) ** 2
slope = num / den; intercept = ym - slope * xm
best_fit_error = f(data,slope,intercept)
best_fit_error = math.sqrt(best_fit_error / len(data))
print "Best estimate for length of the rod at 0 degrees Celsius is %5.2f mm" %(intercept)
print "Coefficient of linear expansion is %5.2f mm/K" %(slope)
print "Error on prediction: %5.2f mm" %(best_fit_error)

#calculating

# Plot best-fit line
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
x = np.linspace(0, 12, 300)
ax1.plot(x, slope * x + intercept, label="Coefficient of expansion = "+str(slope))
for w in data:
	ax1.scatter(float(w), float(data[w]), s=1)

ax1.set_xlabel("Temperatute in Celsius")
ax1.set_ylabel("Length in mm")


fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

#calculating sums required to plot ellipse
xsq = 0; ysq = 0; xy = 0
for w in data:
    xsq += w ** 2
    ysq += data[w] ** 2
    xy += data[w] * w
xsum = xm * len(data)
ysum = ym * len(data)

#plotting the error ellipse
x = np.linspace(slope - .5, slope + .5, 1000)
y = np.linspace(intercept - .5, intercept + .5, 1000)
x, y = np.meshgrid(x, y)

#coefficients for 1sigma error ellipse
A, H, B, G, F, C = xsq, 2*xsum, len(data), -2*xy, -2*ysum, ysq - (best_fit_error ** 2)*len(data)
assert H**2 - 4*A*B < 0

CS = ax2.contour(x, y,(A*x**2 + H*x*y + B*y**2 + G*x + F*y + C), levels=[1,2], colors=['r','b'])
ax2.set_xlabel('m')
ax2.set_ylabel('c')
#making the legend
labels = ['1-sigma', '2-sigma']
for i in range(len(labels)):
    CS.collections[i].set_label(labels[i])
ax2.legend(loc='upper left')
plt.show()
