import turtle
import random

from turtle import Turtle

class Square(Turtle):
	def __init__(self, size, color):
		Turtle.__init__(self)
		self.shapesize(size)
		self.color(color)
		self.shape("square")

	def random_color(self):
		self.color(random)

s = Square(40, "blue")
s.random_color()