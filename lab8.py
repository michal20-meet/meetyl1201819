import turtle
from turtle import *
import random
import math

class ball(Turtle):
	def __init__(self, radius, color, speed, dx, dy):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
		self.dx = dx
		self.dy = dy

	def move(self):
		while True:
			self.pu()
			self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

# D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))


b1 = ball(50, "yellow", 10, 1, 1)
b2 = ball(25, "green", 5, 6, 2)

b1.move()
b2.move()

def check_collision(ball1, ball2):
	# if ball1.pos() == ball2.pos():
	# 	print("there's a collision")
	if math.sqrt(math.pow((ball2.xcor()-ball1.xcor()),2) + math.pow((ball2.ycor()-ball1.ycor()),2)) <= ball1.radius + ball2.radius:
		print("there is a collision")

check_collision(b1, b2)

turtle.mainloop()