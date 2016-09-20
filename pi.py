import matplotlib.pyplot as plt
import numpy as np
times=500
N=2000
expPi=[]
for j in range(times):
    count=0
    for i in range(N):
        x=2*np.random.random(size=N)-1
        y=2*np.random.random(size=N)-1
        if(x[i]**2+y[i]**2<1): #inside circle
            count=count+1
    expPi.append(4.0*count/N)
    #print 4.0*count/N
#print expPi
plt.hist(expPi,bins=np.linspace(2.9,3.3,1000))
plt.show()
