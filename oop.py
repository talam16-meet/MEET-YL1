
class Animal:
	def __init__(self, name, age, color, size):
		self.name=name		
		self.age=age
		self.color=color
		self.size=size
	def print_all(self):
		print(self.name)
		print(self.age)
		print(self.color)
		print(self.size)
	def eat(self,food):
		print("The animal"+ self.name +"is eating" +food)
		
		
dog=Animal("Nour Awwad", 2, "Black", "overweight")
lion=Animal("fff", 3, "Green", "tiny")
coala=Animal("Nina", 1, "Pink", "huge")


dog.print_all()
dog.eat("Pizza")
lion.print_all()
lion.eat("Pasta")
coala.print_all()
coala.eat("Grass")



