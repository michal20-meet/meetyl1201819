import turtle
from turtle import *
import random
import math

class ball(Turtle):
	def __init__(self, radius, color, speed, d):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
		self.d = d

	def move(self):
		while True:
			self.goto(self())
			math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))

b1 = ball(25, "yellow", 10)
b2 = ball(50, "green", 5)

b1.move()
b2.move()

#def check_collision(ball1, ball2):

turtle.mainloop()