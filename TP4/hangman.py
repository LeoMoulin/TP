from hangmantui import *
from userInput import *

def ask_letter_again(used, vies, substitute):
	hangman(vies)
	print(substitute)
	print("Il vous reste " + str(vies) + " vies")
	letter = raw_input("Entrez une lettre : ").lower()
	while (letter in used):
		clear()
		hangman(vies)
		print(substitute)
		print("Il vous reste " + str(vies) + " vies")
		letter = raw_input("Cette lettre est deja utilisee veuillez en entrer une autre : ").lower()
	return letter

def find(letter, word):
	#Retourne un tableau qui contient toutes les positions dune lettre donnee dans un mot
	pos = []
	for i in range(0, len(word)):
		if (letter == word[i]):
			pos.append(i)
	return pos

win = True
word = ask_word_in_dictionary()
vies = 10
usedletters = []

substitute = len(word)*'*'

while('*' in substitute):
	letter = ask_letter_again(usedletters, vies, substitute)
	usedletters.append(letter)
	if letter in word:
		letterpos = find(letter, word)
		
		for i in range(0, len(letterpos)):
			substitute = substitute[0:letterpos[i]] + word[letterpos[i]] + substitute[letterpos[i]+1: len(substitute)]
	else: vies -= 1		
	if (vies == 0):
		clear()
		win = False 
		break
	clear()

if (win):
	print("You won")
else : print("You lost")
