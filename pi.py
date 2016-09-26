import matplotlib.pyplot as plt
import numpy as np
times=500
N=2000
expPi=[]
for j in range(times):
    count=0 #initialise counter
    for i in range(N):
        x=2*np.random.random(size=N)-1 #generate uniformly distributed random x coordinate in the range [-1, 1)
        y=2*np.random.random(size=N)-1 #generate unifromly distributed random y coordinate in the range [-1, 1)
        if(x[i]**2+y[i]**2<1): #inside circle
            count=count+1
    expPi.append(4.0*count/N)
#displaying distribution as a histogram  
plt.hist(expPi,bins=np.linspace(2.9,3.3,1000))
plt.show()
mPi= sum(expPi)/times #mean value of Pi
print ('Estimated value of pi is %f' % (mPi))
varPi=0.0 #to calculate variance
for j in range(times):
    varPi+= (expPi[j] - mPi)**2
varPi/=times
vPi= varPi ** 0.5
print ('Error in estimated value of pi is %f' % (vPi))   