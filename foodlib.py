class foodItem:
	def __init__(self, name, health, nutrition, sanity, type, portion):
		self.nutrition = nutrition
		self.health = health
		self.sanity = sanity
		self.type = type
		self.name = name
		self.portion = portion
		self.specs = []

#a = foodItem('fish', 1,12.5,0,'fish')
#print a.n
#print a.h
#print a.s
#print a.t

types = [Meats, Fishes, Vegetables, Fruits, Monster Food, Eggs, Sweeteners, Dairy]

item1 = foodItem('Wet Goop', 0,0,0,'Not valid',0)
item2 = foodItem('Cooked Green Cap',  -1, 0,15,'Vegetables',0.5)
item3 = foodItem('Rot',  -1, -10, 0,'Not valid',0)
item4 = foodItem('Rotten Egg',  -1, -10, 0,'Not valid',0)
item5 = foodItem('Monster Meat',  -20,18.75, -15,'Meats',1)

#TODO replace all this with a big list 

nameStack = [item1.name, item2.name, item3.name, item4.name, item5.name]
itemStack = [item1, item2, item3, item4, item5]
listErrorString = ("invalid list item, idiot")
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
		if (inputItem in nameStack):
			foodArray.append(inputItem)
			k = nameStack.index(inputItem)
			if (itemStack[k].type != 'Not valid'):
				print "adding " + str(itemStack[k].portion) + " portion(s) of " + str(itemStack[k].type) + " to the possible recipe"
				#add portion to appropriate type
			else:
				print "not a valid food for crock pot use"
		else:
			foodArray.append(listErrorString)
		i = i + 1 
  
aggregateFoodList()	
		
#print item1.n
#print item2.n
#print item3.n
list