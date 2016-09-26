class Polynoomial(object):
	coeffs=[]
	def __init__(self, coefficients):
		self.coeffs=coefficients
	def coeff(self, i):
		return self.coeffs[len(self.coeffs)-i-1]
	def add(self, other):
		newcof=[]
		for i in range(len(sel.coeffs)):
					