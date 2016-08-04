

class Circle(object):
	pi = 3.14
	
	def __init__(self,radius):
		self.radius = radius
		
	def circumference(self):
		circumference = 2 * self.pi * self.radius
		return circumference 
	
	def area(self):
		area = self.pi * self.radius ** 2
		return area
		
angie = Circle(15)
print(angie.area())
print(angie.circumference())