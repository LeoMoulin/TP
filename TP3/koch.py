from uturtle import *

def koch(t, x, seuil):
	if (x < seuil):
		moveForward(t, x)	
		return
	koch(t, x/3, seuil)
	turnLeft(t, 60)

	koch(t, x/3, seuil)
	turnRight(t, 120)
	
	koch(t, x/3, seuil)
	turnLeft(t, 60)

	koch(t, x/3, seuil)


def flocon(t, x, seuil):
	koch(t,x, seuil)
	turnLeft(t, 72)
	koch(t,x, seuil)
	turnLeft(t, 72)
	koch(t,x, seuil)
	turnLeft(t, 72)
	koch(t,x, seuil)
	turnLeft(t, 72)
	koch(t,x, seuil)
	turnLeft(t, 72)

def carre(t, x, seuil):
	if (x < seuil):
		moveForward(t,x)
		return
	carre(t, x/4, seuil)
	turnLeft(t, 90)

	carre(t, x/4, seuil)
	turnRight(t, 90)
	
	carre(t, x/4, seuil)
	turnRight(t, 90)

	carre(t, x/4, seuil)
	turnLeft(t, 90)

	carre(t, x/4, seuil)
bob = umonsTurtle()
carre(bob, 500, 15)
wait()
