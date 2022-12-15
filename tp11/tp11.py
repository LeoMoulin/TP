def plus_grand_bord(w):
	if (len(w) % 2 == 0):
		s1 = w[0:(len(w)/2)]
	else : 
		s1 = w[0:(len(w)/2)+1]
	s2 = w[(len(w)/2):len(w)]
	while (s1 != ""):
		if (s1 == s2):
			return s1
		s1 = s1[0:len(s1)-1]
		s2 = s2[1: len(s2)]
	return None

def intersection(v, w):
	l = 0
	maxn = 0
	resp = ""
	for i in range(0, len(v)):
		n = 0
		while(v[i:i+n] in w):
			n = n+1
			if i+n > len(v):
				break;
			if n > maxn:
				maxn = n
				resp = v[i:i+n-1]
	return resp	

def anagrammes(v, w):
	if (len(v) != len(w)):
		return False
	for i in range(0, len(v)):
		if (v[i] not in w or w[i] not in v):
			return False
	return True

def palindrome(v):
	for i in range(0, (len(v)/2)+1):
		if (v[i] != v[len(v)-i-1]):
			return False
	return True


def chiffrement_vigenere(texte, mot):
	n = 0
	for i in range(len(mot), len(texte)):
		mot = mot + mot[n]
		n+=1
		if (n == len(mot)-1):
			n = 0

	res = ""
	texte = texte.upper()
	for i in range(0, len(mot)):
		decal = ord(mot[i]) - ord("A")
		temp = (((ord(texte[i])%ord("A")) + decal)%26)+ord("A")
		res += chr(temp)
	return res

def dechiffrement_vigenere(texte, mot):
	n = 0
	for i in range(len(mot), len(texte)):
		mot = mot + mot[n]
		n+=1
		if (n == len(mot)-1):
			n = 0
	res = ""
	mot = mot.upper()
	texte = texte.upper()
	for i in range(0, len(mot)):
		decal = ord(mot[i])-ord(texte[i])
		temp = ((26-decal)%26)+ord("A")
		res = res + chr(temp)
	return res
		
print(dechiffrement_vigenere("yzadgqxqmmtpxazvblxitapsgmnedinexsikallqotgvrp", "algorithme"))
	
