import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import math
p=0.3
n=100
for i in range(n+1):
    prob=math.factorial(n)/(math.factorial(i)*math.factorial(n-i))
    plt.plot([i,i],[0,prob],'r')
plt.figtext(0.76,.8,'n=%d\np=%4.2f' %(n,p), fontsize=14 ,bbox=dict(facecolor='red', alpha=0.5))
plt.show()
