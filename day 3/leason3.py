from turtle import *

#drawing houses

width(7)
speed(99)
penup()
goto(50,50)
pendown()

color("green")
begin_fill()
forward(500)
left(180)
forward(1000)
left(90)
forward(500)
left(90)
forward(1000)
left(90)
forward(500)
end_fill()

color("yellow")
penup()
goto(-300,-200)
pendown()

begin_fill()

forward(110)
right(90)
forward(100)
right(90)
forward(110)
right(90)
forward(100)
end_fill()

right(90)
forward(110)
right(35)
forward(90)

penup()
goto(-300,-200)
pendown()

left(35)
forward(110)

color("red")
begin_fill()

right(90)
forward(100)
left(120)
forward(90)
left(114)
forward(90)
end_fill()

penup()
goto(-300,-200)
pendown()

color("yellow")
left(126)
forward(35)

color("brown")
begin_fill()

left(90)
forward(50)
right(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)
 
end_fill() 

penup()
goto(-290,-130)
pendown()

color("white")
begin_fill()

left(180)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)

end_fill()

color("white")

penup()
goto(-230,-130)
pendown()

begin_fill()

left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)

end_fill()

color("red")

penup()
goto(240,-300)
pendown()

begin_fill()

left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

end_fill()

left(180)
forward(100)

color("black")
begin_fill()

right(30)
forward(100)
right(120)
forward(100)
right(120)
forward(100)

end_fill()

color("red")

left(90)
forward(100)
left(90)
forward(35)
left(90)

color("orange")

begin_fill()

forward(50)
right(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)

end_fill()

penup()
goto(150,40)
pendown()

begin_fill()

left(90)
forward(110)
right(90)
forward(100)
right(90)
forward(110)
right(90)
forward(100)

end_fill()

color("grey")
begin_fill()


left(120)
forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(90)

end_fill()

color("orange")

left(180)
forward(110)
right(90)
forward(35)

color("red")
begin_fill()

right(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
left(90)
forward(30)

end_fill()

penup()
goto(150,40)
pendown()

color("grey")

forward(1)

penup()
goto(140,-2)
pendown()

color("white")
begin_fill()


left(180)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)

end_fill()

penup()
goto(60,-2)
pendown()

begin_fill()

left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)


end_fill()
 
color("light blue")

penup()
goto(30,55)
pendown()

begin_fill()

right(90)
forward(500)
right(90)
forward(500)
right(90)
forward(1000)
right(90)
forward(500)
right(90)
forward(500)

end_fill()

penup()
goto(150,40)
pendown()

color("grey")

begin_fill()

right(60)
forward(100)
left(120)
forward(100)

end_fill()

import turtle

speed(50)

screen = turtle.Screen()



y = turtle.Turtle()


def drawFourRays(t, length, radius):
	
	for i in range(4):
		t.penup()
		t.forward(radius)
		t.pendown()
		t.forward(length)
		t.penup()
		t.backward(length + radius)
		t.left(90)



y.penup()
y.goto(-320,200)
y.fillcolor("yellow")
y.pendown()
y.begin_fill()
y.circle(45)
y.end_fill()

y.penup()
y.goto(-320,245)
y.pendown()
drawFourRays(y, 85, 54)
y.right(45)
drawFourRays(y, 85, 54)
y.left(45)


import turtle 
import math 



def drawRectangle(t, width, height, color): 
	t.fillcolor(color) 
	t.begin_fill() 
	t.forward(width) 
	t.left(90) 
	t.forward(height) 
	t.left(90) 
	t.forward(width) 
	t.left(90) 
	t.forward(height) 
	t.left(90) 
	t.end_fill() 

	

def drawTriangle(t, length, color): 
	t.fillcolor(color) 
	t.begin_fill() 
	t.forward(length) 
	t.left(135) 
	t.forward(length / math.sqrt(2)) 
	t.left(90) 
	t.forward(length / math.sqrt(2)) 
	t.left(135) 
	t.end_fill() 

	
 
screen = turtle.Screen ( ) 



tip = turtle.Turtle() 
tip.color ("black") 
tip.speed (10) 



tip.penup() 
tip.goto(-65, -140) 
tip.pendown() 
drawRectangle(tip, 20, 40, "brown") 


tip.penup() 
tip.goto(-100, -100) 
tip.pendown() 
drawTriangle(tip, 90, "lightgreen") 
tip.penup() 
tip.goto(-95, -55) 
tip.pendown() 
drawTriangle(tip, 80, "lightgreen") 
tip.penup() 
tip.goto(-90, -15) 
tip.pendown() 
drawTriangle(tip, 70, "lightgreen")


exitonclick()