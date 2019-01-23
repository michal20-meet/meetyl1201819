from turtle import *

class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)
		self.pu()
		self.shape("circle")
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shapesize(r/10)
		self.color(color)

	def move(self, SCREEN_WIDTH, SCREEN_HEIGHT):
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		up_side_ball = new_y + self.r
		down_side_ball = new_y - self.r
		if (right_side_ball >= SCREEN_WIDTH) or (left_side_ball <= -SCREEN_WIDTH):
			self.dx = -1 * self.dx
		# if left_side_ball <= -SCREEN_WIDTH:
		# 	self.dx = -1 * self.dx
		if (up_side_ball >= SCREEN_HEIGHT) or (down_side_ball <= -SCREEN_HEIGHT) :
			self.dy = -1 * self.dy
		# if down_side_ball <= -SCREEN_HEIGHT:
			# self.dy = -1 * self.dy
		self.goto(new_x,new_y)




