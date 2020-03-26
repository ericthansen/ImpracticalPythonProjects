def main():
    phrase = input('Enter a phrase!\n')
    #phrase_list = phrase.split(' ')
    #print(phrase_list)

    if(phrase == "Hello"):
        print('Hello to you too')
    elif(phrase ==  "What is your name?"):
        print('My name is Computera')
    else:
        print("Say Hello, or ask me my name.")

if __name__ == "__main__":
    main()