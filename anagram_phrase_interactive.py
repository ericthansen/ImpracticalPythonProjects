import load_dictionary
from collections import Counter

word_list = load_dictionary.load('words.txt')
target = 'Eric Tyler Hansen'
#target = input("Enter a word \n")
EXIT = False
while not EXIT:
	phrase_len = 0
	
	LIMIT = len(target)
	anagram_phrase = []
	count = Counter(target)
	while len(anagram_phrase) < LIMIT: