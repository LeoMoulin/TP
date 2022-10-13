#Ok
def caractere(s, i):
	if (i < 1 or i > len(s)):
		return

	return s[i-1]
#Ok
def caracteres(s, i, j):
	if (i < 0 or j > len(s)):
		return None

	res = ""
	for k in range(i, j):
		res += s[k]
	return res
#Ok
def change_caractere(s, i, a):
	if (i < 1 or i > len(s)):
		return None
	return s[0:i-1] + a + s[i:len(s)]

#Ok
def change_caracteres(s, i, j, t):
	if (i < 1 or j > len(s)):
		return None
	return s[0: i-1] + t + s[j:len(s)]

#Ok
def decouvre(s1, s2, x):
	res = ""
	for i in range(0, len(s1)):
		if (s1[i] == x):
			res += x
		else : res += s2[i]
	return res






