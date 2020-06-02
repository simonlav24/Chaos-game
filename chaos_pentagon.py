import random
import turtle
import time


wn = turtle.Screen()
wn.title("chaos")
wn.bgcolor("white")
wn.setup(width = 800, height = 600)
wn.tracer(0)

currentX = 0
currentY = 500

point1 = [0,-200]
point2 = [-190,-62]
point3 = [-118,162]
point4 = [118,162]
point5 = [190,-62]

point = turtle.Turtle()
point.penup()
point.color("red")

#draw first three points:

point.setposition(point1[0],point1[1])
point.dot()
point.setposition(point2[0],point2[1])
point.dot()
point.setposition(point3[0],point3[1])
point.dot()
point.setposition(point4[0],point4[1])
point.dot()
point.setposition(point5[0],point5[1])
point.dot()
#draw starting position

last_point = 0

point.color("blue")
point.setposition(currentX,currentY)
point.dot()

point.color("black")

time1 = time.time()
random.seed((time1	- int(time1))*1000)

def game(lastX,lastY):
	global currentX
	global currentY
	global last_point
	rand = random.randint(1,5)
	x = lastX
	y = lastY
	if rand == 1:
		last_point = 1
		x = (point1[0]+lastX)*(3/8)
		y = (point1[1]+lastY)*(3/8)
	if rand == 2: 
		last_point = 2
		x = (point2[0]+lastX)*(3/8)
		y = (point2[1]+lastY)*(3/8)
	if rand == 3:
		last_point = 3
		x = (point3[0]+lastX)*(3/8)
		y = (point3[1]+lastY)*(3/8)
	if rand == 4:              
		x = (point4[0]+lastX)*(3/8)
		y = (point4[1]+lastY)*(3/8)
	if rand == 5:
		x = (point5[0]+lastX)*(3/8)
		y = (point5[1]+lastY)*(3/8)
		
	point.setposition(x,y)
	point.dot()
	
	currentX = x
	currentY = y
	
#keyboard:
wn.listen()
wn.onkeypress(game(currentX,currentY),"d")

#main loop
while True:
	wn.update()
	game(currentX,currentY)
	
	
	
	
	
	
	
	
	





