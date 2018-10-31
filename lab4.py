#1 + 2
"""class animal(object):
	def __init__(self, sound, name, age, favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color

	def eat(self, food):
		print("yummy!! " + self.name + " is eating " + food)

	def description(self):
		print(self.name + " is " + self.age + " years old and loves the color " + self.favorite_color)

	def make_sound(self):
		print((self.sound + " ")*3)


cat = animal("meow", "katy", "4", "gray")
cat.eat("tuna")
cat.description()
cat.make_sound()"""

#3
class person():
	def __init__(self, name, age, city, gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender

	def fav_breakfast(self, food):
		print( self.name + "	is eating now her favorite food: " + food)

netta = person("Netta", "15", "jerusalem", "female")
netta.fav_breakfast("salad")