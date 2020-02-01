import sys, random

print("Welcome to the 'Sidekick Name Generator.' \n")
print("For funny names usable for comedy, improv, or RPG night.")

first = ('Applejack', 'AaronBurr', 'Baby Arm', 'Chinstrap', 'Colloidal Silver', 'Chitty Chitty Bang Bang', 'Doghouse', 'Dearth', 'Eustus', 
	'Frankenfurter', 'Geneologous', 'Harvey', 'Harrison', 'Itchy Itchy Ichabod', 'And Many More'
	)

last = ('Aardvaar', 'Bluetooth', 'Chattan', 'Derby', 'Elephantitis', 'Flaxseed', 'Garp', 'Hornsby', 'Ichabod', 'Jingle-Jangle Jones', 'Kakarot', 'Looper',
	'Merriadoc', 'Nethermoops', 'O.P. Orangutan', 'Pinkerton', 'Quiescent', 'Ronaldo', 'Stroganofshine', 'Tippletink', 'Underlip', 'Viola', 'Whizbang', 'X-ray-Specs Xanth', 'Zoom, PhD'
	)

while True:
	firstName = random.choice(first)
	lastName = random.choice(last)

	print("/n/n")
	print("{} {}".format(firstName, lastName), file=sys.stderr)
	#print("{} {}".format(firstName, lastName))

	try_again = input("\n\n Try again? (Press Enter else n to quit)\n")
	if try_again.lower()=='n':
		break

input('Press Enter to exit.')