# coding: utf-8
import sys
def lecture(nom):
	res = ""
	with open(nom, 'r') as f:
		lines = f.readlines()
		for l in lines:
			res += l
	return res

def nettoyage(texte):
	allowed = "abcdefghijklmnopqrstuvwxyz"
	res = ""
	for c in texte:
		if c.lower() in allowed:
			res += c.lower()
	return res 

def chiffrement_decallage(f, u):
	texte = nettoyage(lecture(f))
	res = ""	
	for c in texte:
		n = (ord(c)- 96 + u)%25
		res += chr(n+ 96)
	return res

def dechiffrement_decallage(f, u):
	texte = nettoyage(lecture(f))
	res = ""	
	for c in texte:
		n = (ord(c)- 96 - u)%26
		res += chr(n + 96)
	return res

def chiffrement_substitution(f, dico):
	texte = nettoyage(lecture(f))
	s = nettoyage(lecture(dico))
	i = 0
	dic = dict()
	while(i < len(s)):
		dic[s[i]] = s[i+1]
		i += 2
	res = ""	
	for c in texte:
		res += dic[c]
	return res

def dechiffrement_substitution(f, dico):
	texte = nettoyage(lecture(f))
	s = nettoyage(lecture(dico))
	i = 1
	dic = dict()
	while(i < len(s)):
		dic[s[i]] = s[i-1]
		i += 2
	res = ""	
	print(dic)
	for c in texte:
		if c in dic:
			res += dic[c]
		else:
			res += c
	return res

def decouvre_cle(text, i):
	frenchfreq = {'a' : 9.42, 'b' : 1.02, 
                      'c' : 2.64, 'd' :3.39, 'e': 15.87, 'f' : 0.95, 'g': 1.04, 'h':0.77, 'i':8.41, 'j':0.89,
                      'k': 0.0, 'l' : 5.34, 'm' : 3.24, 'n': 7.15, 'o':5.14, 'p':2.86, 'q':1.06, 'r':6.46, 's':7.90, 't':7.26,'u':6.24, 'v':2.15,
                      'w': 0.0, 'x': 0.30, 'y':0.24, 'z':0.32}
	sortedfreq = sorted(frenchfreq.items(), key=lambda x:x[1], reverse=True)
	texte = lecture(text)
	lettercount = dict()
	for k in range(97, 97+26):
		lettercount[chr(k)] = 0	
	
	for c in texte: 
		lettercount[c] += 1
	
	for m in range(97, 97+26):
		lettercount[chr(m)] = lettercount[chr(m)]/len(text)
	
	target = ""
	for j in range(0, i):
		target += sortedfreq[j][0]
	
	result = dict()
	sortedlcount = sorted(lettercount.items(), key=lambda x:x[1], reverse=True)
	for p in range(0, len(target)):
		result[target[p]] = sortedlcount[p][0]
	return result



print(decouvre_cle("analyse.txt", 10))

"""
if (sys.argv[1] == 'd') and (sys.argv[2] == 'c'):
	print(chiffrement_decallage(sys.argv[3], int(sys.argv[4])))

if (sys.argv[1] == 'd') and (sys.argv[2] == 'd'):
	print(dechiffrement_decallage(sys.argv[3], int(sys.argv[4])))

if (sys.argv[1] == 's') and (sys.argv[2] == 'c'):
	print(chiffrement_substitution(sys.argv[3], sys.argv[4]))

if (sys.argv[1] == 's') and (sys.argv[2] == 'd'):
	print(dechiffrement_substitution(sys.argv[3], sys.argv[4]))
"""
