"""
Prints list of anagrams (in given dictionary) of a user-provided word
"""

import load_dictionary

word_list = load_dictionary.load('words.txt')
word = 'Foster'
#word = input("Enter a word")

anagram_list = []

word_sorted = sorted(word.lower())#sorted(list(word.lower()))

for w in word_list:
	w_sorted = sorted(list(w.lower()))
	if w_sorted == word_sorted and w.lower() != word.lower():
		anagram_list.append(w)
print('Anagrams: ', *anagram_list, sep = '\n')