def has_duplicates(list1):
	l=len(list1)
	for i in range(l):
		for j in range(i+1, l):
			if list1[i]==list1[j]:
				return True
	return False

print has_duplicates([1,2,3,5,4,6,6])
print has_duplicates([1,2,3])				