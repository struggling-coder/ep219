import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import math
mu=[0,1.5,0,0]
sigma=[.75,.75,1,0.5]
x = np.linspace(-4,4,160)
for i in range(4):
    plt.plot(x,mlab.normpdf(x,mu[i],sigma[i]), label='$\mu={i},\sigma={j}$'.format(i=mu[i],j=sigma[i]))
plt.legend(loc='best')
plt.show()
