import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import math

l=10 #parameter lambda
for i in range(0, 100):
    prob=math.exp(-l) * math.pow(l,i) / math.factorial(i) #evaluating value at i
    plt.plot([i,i],[0,prob],'r') #plotting graph
#textbox and graph display
plt.figtext(0.79,.8,'$lambda=%d$' %(l), fontsize=14 ,bbox=dict(facecolor='red', alpha=0.1),horizontalalignment='center',verticalalignment='center')
plt.show()

