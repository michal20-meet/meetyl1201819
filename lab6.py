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


#2

class hexagon(Turtle):
	def __init__(self, size, color):
		Turtle.__init__(self)

		turtle.home()
		turtle.begin_poly()
		i = 6
		turtle.pu()
		for i in range(6):
			turtle.fd(size)
			turtle.left(60)
		turtle.end_poly()
		hexagon = turtle.get_poly()
		turtle.register_shape("hexagon", hexagon)

		self.color(color)
		self.shape("hexagon")


h = hexagon(400, "red")


turtle.mainloop()