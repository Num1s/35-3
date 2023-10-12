
class Calculator(object):
	def __init__(self, num):
		self.num = num

	def __add__(self, other):
		return self.num + other.num

	def __sub__(self, other):
		return self.num - other.num

	def __mul__(self, other):
		return self.num * other.num

	def __truediv__(self, other):
		return self.num / other.num