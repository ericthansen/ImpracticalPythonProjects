import sys
import random
def main():
    """Chooses names at random from 2 tuples of names and prints to screen."""
    print("Welcome to the 'Sidekick Name Generator.' \n")
    print("For funny names usable for comedy, improv, or RPG night.\n\n")

    first = ('Applejack', 'AaronBurr', 'Baby Arm', 'Chinstrap', 'Colloidal Silver', 'Chitty Chitty Bang Bang', 'Doghouse', 'Dearth', 'Eustus', 
        'Frankenfurter', 'Geneologous', 'Harvey', 'Harrison', 'Itchy Itchy Ichabod', 'And Many More'
        )

    last = ('Aardvaar', 'Bluetooth', 'Chattan', 'Derby', 'Elephantitis', 'Flaxseed', 'Garp', 'Hornsby', 'Ichabod', 'Jingle-Jangle Jones', 'Kakarot', 'Looper',
        'Merriadoc', 'Nethermoops', 'O.P. Orangutan', 'Pinkerton', 'Quiescent', 'Ronaldo', 'Stroganofshine', 'Tippletink', 'Underlip', 'Viola', 'Whizbang', 'X-ray-Specs Xanth', 'Zoom, PhD'
        )

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)

        print("/n/n")
        print("{} {}".format(first_name, last_name), file=sys.stderr)
        #print("{} {}".format(firstName, lastName))

        try_again = input("\n\n Try again? (Press Enter else n to quit)\n")
        if try_again.lower()=='n':
            break

    input('Press Enter to exit.')

if __name__ == "__main__":
    main()