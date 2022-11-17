def bubblesort(l):
	for i in range(0, len(l)):
		l = list(l)
		for j in range(0, len(l)-1-i):
			if (l[j] > l[j + 1]):
				temp = l[j]
				l[j] = l[j+1]
				l[j + 1] = temp

	return l

print(bubblesort((6, 5, 4, 3, 14 ,15 ,3,6)))

