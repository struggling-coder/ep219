def rotate_word(orig_word):
	new_word=''
	for letter in orig_word:
		c=ord(letter)
		if (c<=109 and c>=97) or (c<=77 and c>=65):
			new_word+=(chr(c+13))
		elif (c>109 and c<=122) or (c>77 and c<=90):
			new_word+=(chr(c-13))
		else:
			new_word+=chr(c)	
	return new_word
	
print rotate_word("lemon melon")			