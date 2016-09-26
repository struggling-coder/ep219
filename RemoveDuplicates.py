def remove_duplicates(list1):
	list2=[]
	for element in list1:
		if element not in list2:
			list2.append(element)
	return list2
	
print remove_duplicates([1,2,3,4,5,6,4,2,6,8,7,9,1,3,4,6,1,6,7,0,5,3])			