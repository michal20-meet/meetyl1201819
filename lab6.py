import turtle
import random
from turtle import Turtle

#1
# turtle.colormode(255)

# class Square(Turtle):
# 	def __init__(self, size, color):
# 		Turtle.__init__(self)
# 		self.shapesize(size)
# 		self.color(color)
# 		self.shape("square")

# 	def random_color(self):
# 		self.color(random.randint(0,256), random.randint(0,256),random.randint(0,256))

# s = Square(15,"yellow")
# s.random_color()

turtle.begin_poly()
turtle.fd(100)
turtle.left(20)
turtle.fd(30)
turtle.left(60)
turtle.fd(50)
turtle.end_poly()
p = turtle.get_poly()

class hexagon(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.
turtle.mainloop()