from uturtle import *

def tree(t, angle, distance, n, coeff, maxn=0):
	maxn = max(maxn, n)
	
	turnLeft(t, angle)
	moveForward(t, distance)

	if (n==0):
		moveBackward(t,distance)
		return
	
	tree(t, 30, distance/2, n-1, 0, maxn)
	tree(t, 300, distance/2, n-1, 1, maxn)
	
	if (not coeff):
		turnLeft(t, angle)	
	else:
		turnLeft(t, 360-angle-30)

	if (maxn != n):
		moveBackward(t,distance)
	return	

bob = umonsTurtle()
tree(bob, 90, 100, 3, 0)
wait()
