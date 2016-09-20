import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import math
p=0.3
n=100
for i in range(n+1):
    prob=math.factorial(n)/(math.factorial(i)*math.factorial(n-i))
    plt.plot([i,i],[0,prob],'r')
plt.show()
