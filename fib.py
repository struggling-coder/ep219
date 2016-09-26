class V2(object):
	def __init__(self, x, y):
		self.x=x
		self.y=y
	def __str__(self):
		return '('+str(self.x)+', '+str(self.y)+')'
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def add(self, other):
		return V2(self.x+other.x, self.y+other.y)
	def __add__(self, other):
		return self.add(other)
	def mul(self, scalar):
		return V2(scalar*self.x, scalar*self.y)
	def __mul__(self, scalar):
		return self.mul(scalar)	

p1=V2(2,3)
p2=V2(-1, -2)
print p1
print p2
print p1.getX()+p2.getY()
print p1.add(p2)
print p1*5
p1+p2*2