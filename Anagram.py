def is_anagram(word1, word2):
	word1=list(word1)
	word2=list(word2)
	word1.sort()
	word2.sort()
	if word1==word2:
		return True
	return False
	
print is_anagram("stop", "post")
print is_anagram("banana", "ban")		