"""
Given a user inputted word or name, allows user to select/design various possible anagram phrases.
"""

import load_dictionary
from collections import Counter

word_list = load_dictionary.load('words.txt')
target = 'Eric Tyler Hansen'
#target = input("Enter a word \n")
LIMIT = len(target)
anagram_phrase = []
count = Counter(target)
while len(anagram_phrase) < LIMIT:
	for word in word_list:
		next_word_options = []
		count_word = Counter(word)
		contained = True
		for key, value in count_word:
			if value >= count[key]:
				contained = False
				break
		if contained :
			next_word_options.append(word)
	print('\nNext word choices include:', *next_word_options, sep = '\n')
	
	next_word = None
	while !next_word:
		try:
			next_word = input('Please select from those options:\n')
			if next_word not in next_word_options:
				print("Not a valid choice, please select from the options above.\n")
				next_word = None
		except:
			print("Error handling")
	



