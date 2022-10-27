from random import *

def creer_enchevetrements(bag, i, max_enchevetrements):
	number = randint(1, max_enchevetrements)
	res = []
	for k in range(0, number):
		x = randint(0, len(bag))
		res.append((x, i)) 
	return list(set(res))

def creer_mikado(bag):
	res = []
	for i in range(1,len(bag)):
		res += creer_enchevetrements(bag, i, len(bag))
	return res

def peut_retirer(i, bag, jeu):
	for a in jeu:
		if a[0] == i:
			return False
	return True		

def quel_ordre(bag, jeu):	
	if (len(bag) == 1):	
		return [bag[0]]

	for i in bag:
		if peut_retirer(i, bag, jeu):
			newbag = [j for j in bag if j != i]
			newgame = [k for k in jeu if k[1] == i]
			return [i] + quel_ordre(newbag, newgame)
			
	
def est_jouable(bag, jeu):	
	if (len(bag) == 1):	
		return True

	for i in bag:
		if peut_retirer(i, bag, jeu):
			newbag = [j for j in bag if j != i]
			newgame = [k for k in jeu if k[1] == i]
			return est_jouable(newbag, newgame)
	return False
	

l = creer_mikado((0, 1, 2, 3))
print(est_jouable(range(0, 4),l))
print(quel_ordre(range(0, 4),l))



	
