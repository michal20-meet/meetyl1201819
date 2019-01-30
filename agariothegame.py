import turtle
import time
import random
import math
import agario
from agario import Ball

turtle.tracer(0,0)
turtle.hideturtle()
turtle.bgcolor("light green")

RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()//2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()//2

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 50
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
	while x in range(-100,100):
		x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	while y in range(-100,100):
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
	D = math.sqrt(math.pow((ball_b.xcor()-ball_a.xcor()),2) + math.pow((ball_b.ycor()-ball_a.ycor()),2))
	if (D <= ball_a.r + ball_b.r):
		return True
	else:
		return False


def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b):
				radius_a = ball_a.r
				radius_b = ball_b.r
				newX = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				newY = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				newDx = 0
				newDy =0
				while newDx == 0:
					newDx = random.randint(MINIMUM_BALL_DX, MAXMUM_BALL_DX)
				while newDy == 0:   
					newDy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				newRadius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				newColor = (random.random(), random.random(), random.random())
				if radius_a < radius_b:
					ball_a.goto(newX,newY)
					ball_a.dx = newDx
					ball_a.dy = newDy
					ball_a.r = newRadius
					ball_a.color = newColor
					ball_a.shapesize((ball_a.r)/10)
					if ball_b.r < MAXIMUM_BALL_RADIUS:	
						ball_b.r = radius_b+1
						ball_b.shapesize((ball_b.r)/10)
				if radius_a > radius_b:
					ball_b.goto(newX,newY)
					ball_b.dx = newDx
					ball_b.dy = newDy
					ball_b.r = newRadius
					ball_b.color = newColor
					ball_b.shapesize((ball_b.r)/10)
					if ball_a.r < MAXIMUM_BALL_RADIUS:
						ball_a.r = radius_a+1
						ball_a.shapesize((ball_a.r)/10)


def check_myball_collision():
	for ball_b in BALLS:
		if collide(my_ball,ball_b):
			my_radius = my_ball.r
			radius_b = ball_b.r
			newX = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			newY = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			newDx = 0
			newDy =0
			while newDx == 0:
				newDx = random.randint(MINIMUM_BALL_DX, MAXMUM_BALL_DX)
			while newDy == 0:   
				newDy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
			newRadius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
			newColor = (random.random(), random.random(), random.random())
			if my_radius < radius_b:
				return False
			if my_radius > radius_b:
				ball_b.goto(newX,newY)
				ball_b.dx = newDx
				ball_b.dy = newDy
				ball_b.r = newRadius
				ball_b.color = newColor
				ball_b.shapesize((newRadius)/10)
				my_ball.r = my_radius + 1
				my_ball.shapesize((my_ball.r)/10)
	return True

def movearound(event):
        x = event.x - SCREEN_WIDTH
        y = SCREEN_HEIGHT - event.y
        my_ball.goto(x,y)
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while RUNNING == True:
	SCREEN_WIDTH = turtle.getcanvas().winfo_width()//2
	SCREEN_HEIGHT = turtle.getcanvas().winfo_height()//2

	move_all_balls()
	check_all_balls_collision()
	RUNNING = check_myball_collision()
	turtle.update()
	time.sleep(SLEEP)

 
turtle.mainloop()