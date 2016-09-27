import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import math
p=0.8 #parameter p
n=10 #parameter n
for i in range(n+1):
    prob=math.factorial(n)/(math.factorial(i)*math.factorial(n-i)) * math.pow(p, i) * math.pow(1-p, n-i) #evaluating value at i
    plt.plot([i,i],[0,prob],'g') #plotting graph
#textbox and graph display
plt.figtext(0.79,.8,'$n=%d$\n$p=%4.2f$' %(n,p), fontsize=14 ,bbox=dict(facecolor='red', alpha=0.1),horizontalalignment='center',verticalalignment='center')
plt.show()
