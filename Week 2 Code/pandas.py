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
width = math.sqrt( count2 / index - mean ** 2 ) # sample width
sd = width * math.sqrt( index / (index - 1) ) # best estimate for standard deviation on a single measurement
sd_mean = sd / math.sqrt(index) # standard deviation on mean
print "Mean weight: %5.2f kg\nError on the mean weight: %5.2f kg" %(mean, sd_mean)
print "Typical fluctuation of weight of each baby panda: %5.2f kg" %(sd)
print "Sample width: %5.2f kg" %(width)
