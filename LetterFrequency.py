def most_frequent(string1):
	l=list(string1)
	d=dict()
	for c in l:
		if c not in d:
			d[c]=1
		else:
			d[c]+=1
	l2=[]
	for c in d:
		l2.append((d[c], c))
	l2.sort(reverse=True)
	for t in l2:
		print t[1]
		
most_frequent( "Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at")					