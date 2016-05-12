class foodItem:
	def __init__(self, name, health, nutrition, sanity, type):
		self.n = nutrition
		self.h = health
		self.s = sanity
		self.t = type
		self.specs = []

a = foodItem('fish', 1,12.5,0,'fish')
#print a.n
#print a.h
#print a.s
#print a.t

def aggregateFoodList():
	foodArray = []
	inputItem = 'foo'
	i = 0
	while (inputItem != 'fin'):
		j = 0
		print 'Your current list of foods is'
		while (j < i):
			print foodArray[j]
			j = j + 1 
		print 'Please enter a food item, or enter ' + 'fin.' 
		inputItem = raw_input()
		foodArray.append(inputItem)
		i = i + 1 

aggregateFoodList()	
		
