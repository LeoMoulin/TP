class Rational():
	def __init__(self, a=0, b=1):
		if (b == 0):
			raise ZeroDivisionError("Error can't divide by zero")	

		if (type(a) == float and b == 1):
			b = 1
			while (a%1 != 0.0):
				a *= 10
				b *= 10
				
		elif(type(a) != int):
			raise TypeError("Error numerator is " + str(type(a)))
		elif(type(b) != int):
			raise TypeError("Error denominator is " + str(type(b)))	

		if b < 0:
			b = abs(b)
			a = -a
		
		res = 1	
		for i in range(1, min(abs(int(a)),abs(int(b)))+1):
			if (a%i == 0 and b%i == 0):
				res = i		
			
	
		self.num = int(a)//res
		self.denom = int(b)//res

		
 			
	def __str__(self):
		if (self.denom == 1):
			return str(self.num)
		return str(self.num) + '/' + str(self.denom) 
	

	def get_denominator(self):
		return str(self.denom)

	def __repr__(self):
		#return "Rational("+str(self.num)+","+str(self.denom)+")"
		return str(self.num) + '/' + str(self.denom) 

	def __add__(self, other):
		if (type(other) == int):
			other = Rational(other)
		if (type(other) == float):
			other = Rational(other)
		n = 0
		newdenom = max(self.denom, other.denom)
		while n == 0:
			if newdenom % self.denom == 0 and newdenom % other.denom == 0:
				n = newdenom
			newdenom += 1
		selfcoeff = n/self.denom
		othercoeff = n/other.denom
		return Rational((selfcoeff*self.num)+(othercoeff*other.num), n)

	def __mul__(self, other):
		if (type(other) == int):
			other = Rational(other)
		if (type(other) == float):
			other = Rational(other)
		
		return Rational(self.num*other.num, self.denom*other.denom)

	def __radd__(self, other):
		return self+other
	
	def __rmul__(self, other):
		return self*other

	def __float__(self):
		return self.num/self.denom
