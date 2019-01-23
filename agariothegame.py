import turtle
import time
import random
import math
import agario
from agario import Ball

turtle.tracer(1)
turtle.hideturtle()

RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

######################################

my_ball = Ball(20,10,3,3,30,"blue")
# while True:
#my_ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

BALLS = []

for ball in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX, MAXMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	new_b = Ball(x, y, dx, dy, radius, color)
	BALLS.append(new_b)


def move_all_balls():
	for new_b in BALLS:
		new_b.move(SCREEN_WIDTH, SCREEN_HEIGHT)


def collide(ball_a, ball_b):
	if ball_a == ball_b:
		return False
	D = math.sqrt(math.pow((ball_b.x-ball_a.x),2) + math.pow((ball_b.y-ball_a.y),2))
	if (D + 10 <= ball_a.radius) or (D +10 <= ball_b.radius):
		return True
	else:
		return False


turtle.mainloop()