import math

#Ok
def droite(p1, p2):
	if (p1 == p2):
		return None
	if (p1[0] == p2[0]):
		return (1, 0, 0)
	a = (p2[1]-p1[1])/(p2[0]-p1[0])
	c = p1[1]-(a*p1[0])
	return (a, 1, c)

#Ok
def appartient(d, p):
	if (d[0]*p[0]) + (d[1]*p[1]) == d[2]:
		return True
	else :
		return False

#Ok
def paralleles(d1, d2):
	m1 = -(d1[0]/d1[1])
	m2 = -(d2[0]/d2[1])
	if m1 == m2:
		return True
	else: 
		return False

def intersection(d1, d2):
	if (d1 == d2):
		return None
	a1, b1, c1 = d1
	a2, b2, c2 = d2
	
	a1 = a1/b1 
	c1 = c1/b1

	a2 = a2/b2
	c2 = c2/b2
	if a2-a1 == 0:
		return None
	x = -(c2-c1)/(a2-a1)
	y = a1*x + c1
	return (x, y)
#Ok
def droite_normale(d,p):
	(a1, b1, c1) = d
	if (b1 == 0):
		return(0,1,-p[1])
	elif a1 == 0:
		return(1, 0, -p[0])
	b2 = -b1
	a2 = (b2*b1)/a1
	c2 = -a2*p[0]-b1*p[1]
	return(a2, -b2, -c2)


#OK
def distance_droite_point(d, p):
	if (appartient(d,p)):
		return 0
	(x,y) = p
	a, b, c = d
	return abs(a+b+c)/math.sqrt(a**2 + b**2) 

def symetrie_orthogonale(d, p):
	dinter = droite_normale(d, p)
	center = intersection(dinter, d)
	vec = (p[0] - center[0], p[1]-center[1])
	vec = (-vec[0], -vec[1])
	return (p[0]+vec[0], p[1]+vec[1])

print(symetrie_orthogonale((-0.5, 1, 1.0), (-2, 0)))
print(symetrie_orthogonale((-0.5, 1, 1.0), (3, 4)))
