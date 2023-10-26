class Hello(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

class Hi(Hello):
	pass