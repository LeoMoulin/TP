from umage import *

img = [[(255, 255, 255), (30, 0, 255), (30, 0, 255), (0, 0, 0)],
[(30, 0, 255), (0, 255, 0), (0, 255, 0), (255, 0, 0)],
[(255, 0, 0), (30, 0, 255), (30, 0, 255), (255, 0, 0)],
[(0, 255, 0), (30, 0, 255), (30, 0, 255), (255, 0, 0)],
[(0, 0, 0), (0, 255, 0), (30, 0, 255), (255, 0, 0)],
[(0, 0, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0)]]

test = [[0, 1, 0], [1, 0, 1], [1, 1, 1]]

def greyscale(img):
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			val = int((0.2125*img[i][j][0]) + (0.7154*img[i][j][1]) + (0.0721*img[i][j][2]))
			img[i][j] = (val, val, val)
	return img

def formatmatrix(l, newdim):
	horizontaladd = newdim[1]-len(l[0])
	verticaladd = newdim[0]-len(l)

	newlist = l
	
	for i in range(0, verticaladd//2):
		newlist.insert(0, [])
		for j in range(0, newdim[1]-1):
			newlist[0].append((0, 0, 0))

	for i in range(verticaladd//2, verticaladd//2 + len(l)):
		for j in range(0, horizontaladd//2):
			newlist[i-1].insert(0, (0, 0, 0))
		for j in range(horizontaladd//2 + len(l[0]), horizontaladd//2 + len(l[0]) + horizontaladd//2):
			newlist[i-1].append((0, 0, 0))
	
	for i in range(verticaladd//2 + len(l), verticaladd//2 + len(l) + verticaladd//2):
		newlist.append([])
		for j in range(0, newdim[1]):
			newlist[len(newlist)-1].append((0, 0, 0))

	return newlist

def convolution(mat_img, application):	
	#Formates la matrice 
	start = mat_img[0][0]
	newm = formatmatrix(mat_img, (len(mat_img)+(len(application)), len(mat_img[0])+(len(application[0]))))	

	#Definis le point de départ
	startx = len(application)//2 
	starty = len(application[0])//2
	
	#application de la matrice sur chaque tuple
	return newm

def pixel(img, i, j, default):
	height = len(img)
	width = len(img[0])
	if 0 <= i < height and 0 <= j < width:
		return img[i][j]
	else:
		return default


img = greyscale(img)
matimg = load("./image_test(1).jpg")

app = [[-2,0,0],[0,1,0],[0,0,2]]
conv = convolution(matimg, app)
save(conv, "testconv", "jpg")






