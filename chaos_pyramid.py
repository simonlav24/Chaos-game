import random
import turtle
import time
import math

wn = turtle.Screen()
wn.title("pyramid")
wn.bgcolor("white")
wn.setup(width = 800, height = 600)
wn.tracer(0)
cgh;kdngdlgnkdflkgn
pi = 3.1415926
angle = 0.2

point = turtle.Turtle()
point.penup()
point.color("red")

def rot(poin,angle):
	x = poin[0]
	y = poin[1]
	z = poin[2]

	return [ x*math.cos(angle) - y*math.sin(angle) ,\
	x*math.sin(angle) + y*math.cos(angle) ,z]

def p(x,y,z):
	return [(x+y)*math.cos(angle) + (x-y)*math.sin(angle) ,\
	(x*math.cos(angle) - y*math.sin(angle))*math.tan((5*pi)/6) + \
	(x*math.sin(angle) + y*math.cos(angle))*math.tan(pi/6) + (2/math.sqrt(3))*z]

#dis point:
disPoint = [500,-500,500]
print(disPoint)
print(p(disPoint[0],disPoint[1],disPoint[2]))
point.color("orange")
point.setposition(p(disPoint[0],disPoint[1],disPoint[2]))
point.dot()

def rangeMapper(A,B,C,D,X):
	return (((X - A)/(B - A))*(D - C) + C )

def setPosDot(x,y,z):
	global disPoint
	global point
	a = disPoint[0]
	b = disPoint[1]
	c = disPoint[2]
	
	#calculate distance:
	dist = math.sqrt( (x - a)*(x - a) + (y - b)*(y - b) + (z - c)*(z - c) )
	dist2 = rangeMapper(600,1000,7,3,dist)
	
	point.setposition(p(x,y,z)[0],p(x,y,z)[1])
	point.dot(dist2)


#pyramid draw origin:
point.color("red")
pointA = rot([0,-300,-100],angle)
setPosDot(pointA[0],pointA[1],pointA[2])
pointB = rot([-260,150,-100],angle)
setPosDot(pointB[0],pointB[1],pointB[2])
pointC = rot([260,150,-100],angle)
setPosDot(pointC[0],pointC[1],pointC[2])
pointD = rot([0,0,200],angle)
setPosDot(pointD[0],pointD[1],pointD[2])

#initial point:
point.color("blue")
setPosDot(0,0,0)

#game:
time1 = time.time()
random.seed((time1	- int(time1))*1000)
curX = 0
curY = 0
curZ = 0
point.color("black")

def game(lastX,lastY,lastZ):
	global point
	global curX
	global curY
	global curZ
	x = lastX
	y = lastY
	z = lastZ
	
	rand = random.randint(1,4)
	if rand == 1:
		x = (curX + pointA[0])/2
		y = (curY + pointA[1])/2
		z = (curZ + pointA[2])/2
	if rand == 2:
		x = (curX + pointB[0])/2
		y = (curY + pointB[1])/2
		z = (curZ + pointB[2])/2
	if rand == 3:
		x = (curX + pointC[0])/2
		y = (curY + pointC[1])/2
		z = (curZ + pointC[2])/2
	if rand == 4:
		x = (curX + pointD[0])/2
		y = (curY + pointD[1])/2
		z = (curZ + pointD[2])/2
		
	setPosDot(x,y,z)
	
	curX = x
	curY = y
	curZ = z


#main loop
while True:
	wn.update()
	game(curX,curY,curZ)
	
