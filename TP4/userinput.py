
def belongs_to_dictionary(word):
	with open("words.txt") as file:
		for line in file:
			if line.strip() == word.lower():
				return True
	return False

def ask_word_in_dictionary():
	word = ""
	while (not belongs_to_dictionary(word)):
		word = raw_input("Entrez un mot: ").lower()
        return word

def ask_letter(tried_letters):
	letter = ""
	while (not letter in tried_letters):
		letter = raw_input("Entrez une lettre : ").lower()
	return letter



