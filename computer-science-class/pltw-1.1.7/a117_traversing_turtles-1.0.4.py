#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import random
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.speed(0)
  t.penup()
  t.color(turtle_colors.pop())
  my_turtles.append(t)

#  sets up the starting x and y position
startx = 0
starty = 0
startHeading = 0
count = 0

#sets the turtles position to startx, starty and puts the pen down. makes the turtle turn right 45 degreese and move forward 50 something
for t in my_turtles:
  t.goto(startx, starty)
  t.setheading(startHeading)
  t.pendown()   
  t.forward(50*1.05**(count+1))
  count+=1

#sets the start position to where the current turtle ends
  startx = t.xcor() 
  starty = t.ycor()
  startHeading = t.heading()

wn = trtl.Screen()
wn.mainloop()