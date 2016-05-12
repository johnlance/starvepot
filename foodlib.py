class Food:
	def __init__(self, health, nutrition, sanity, type):
		self.n = nutrition
		self.h = health
		self.s = sanity
		self.t = type
		self.specs = []

a = Food(1,12.5,0,'fish')
print a.n
print a.h
print a.s
print a.t
