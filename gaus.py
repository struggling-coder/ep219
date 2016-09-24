import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
mu=[0,1.5,0,0] #set of different mean values
sigma=[.75,.75,1,0.5] #set of different standard deviations
x = np.linspace(-4,4,160) #range of x for which to be plotted
for i in range(4):
    plt.plot(x,mlab.normpdf(x,mu[i],sigma[i]), label='$\mu={i},\sigma={j}$'.format(i=mu[i],j=sigma[i])) #graph plotting
plt.legend(loc='best') #display legend
plt.show()
