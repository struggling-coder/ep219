import math

# Initialize variables and the source of data (pandas.txt)
DATA = './pandas.txt'
count=0; count2=0; index=0; fluctuation=0; values=[]

# Read data from pandas.txt
for e_raw in file.read(open(DATA)).split('\r\n'):
	e=float(e_raw); values.append(e)
	count+=e; count2+=e*e; index+=1

# Calculate and display the required output
mean = count / index # mean
sd = math.sqrt( count2 / index - mean ** 2 ) # standard deviation
fluctuation = sum([abs(e - mean) / index for e in values])
print "Mean weight: %5.2f kg\nError on the mean weight: %5.2f kg" %(mean, sd)
print "Typical fluctuation about mean: %5.2f kg" %(fluctuation)
