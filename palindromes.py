"""Find palindromes (letter palingrams) in a dictionary file."""

import load_dictionary

word_list = load_dictionary.load('words.txt')
pali_list = []

for word in word_list: 
	if word == word[::-1] and len(word) > 1:
		pali_list.append(word)
print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')
#print(pali_list)