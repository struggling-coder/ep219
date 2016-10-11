import math

# Initialize variables and the source of data (pandas.txt)
DATA = './pandas.txt'
count=0; count2=0; index=0

# Read data from pandas.txt
for e_raw in file.read(open(DATA)).split('\r\n'):
	e=float(e_raw)
	count+=e; count2+=e*e; index+=1

# Calculate and display the required output
mean = count / index # mean
sd = math.sqrt( count2 / index - mean ** 2 ) # standard deviation
print "Mean weight: "+str(mean)+"kg\nError on the mean weight: ??"
print "Typical fluctuation about mean: "+str(sd)+"kg"
