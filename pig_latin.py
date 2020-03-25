import sys
import random
def main():
    cons = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    vows = ['A', 'E', 'I', 'O', 'U']

    phrase = input('Enter a phrase!\n')
    #phrase = "Testing, you see, my 'awesome' program."
    phrase_list = phrase.split(' ')
    #print(phrase_list)
    phrase_out = ''
    word_count = len(phrase_list)
    i = 1
    #print(phrase_list)
    for word in phrase_list:
        start_punct = None
        end_punct = None
        #if i == word_count:
        #    word = word[:-1]
            #print('lastword',new_word)

        #checking for punctuation at beginning and end
        if word[0].upper() not in cons and word[0].upper() not in vows:
            start_punct=word[0]
            word = word[1:]
        if word[-1].upper() not in cons and word[-1].upper() not in vows:
            end_punct=word[-1]
            word = word[:-1]
        if word[0].upper() in cons:
            new_word = word[1:] + word[0].lower()+'ay'
            if i == 1:
                new_word = new_word[0].upper() + new_word[1:]
        elif word[0].upper() in vows:
            new_word = word+'way'

        if start_punct:
            new_word = start_punct + new_word
        if end_punct:
            new_word = new_word + end_punct


        phrase_out = phrase_out + new_word + ' '
        i += 1
    phrase_out = phrase_out.strip()
    print(phrase_out)


if __name__ == "__main__":
    main()