def cumulative_sum(list1):
	list2=[]
	for i in range(len(list1)):
		if i==0:
			list2.append(list1[i])
		else:
			list2.append(list1[i]+list2[i-1])
	return list2

print cumulative_sum([x**2 for x in range(1, 11)]) 				