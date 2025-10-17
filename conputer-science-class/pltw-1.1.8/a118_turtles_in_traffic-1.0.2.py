# CODE TO COPY
#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

from numpy import square

# create two empty lists of turtles, adding to them later
horiz_turtles:list[trtl.Turtle] = []
vert_turtles:list[trtl.Turtle] = []



# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
  #creating horizontal turtles
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)
  #creating vertical turtle
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  #changes the location 
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions
"""
for step in range(50):
	# do something
"""
print(trtl.screensize())
def moveTurtles(distance):
  for turtle in trtl.turtles():
    if(turtle.xcor()+distance < 0 and turtle.ycor()-distance > 0 and turtle.fillcolor != "#00ffff"):
      turtle.forward(distance)
    else:
      turtle.color("#00ffff")   

def checkColisions():
  for horizontal_turtle in horiz_turtles:
    for vertical_turtle in vert_turtles:
      if(horizontal_turtle.distance(vertical_turtle) <= 20):
        old_shapes = [horizontal_turtle.shape(), vertical_turtle.shape()]
        old_colors = [horizontal_turtle.fillcolor(), vertical_turtle.fillcolor()]
        horizontal_turtle.color("#ff0000")
        horizontal_turtle.shape("square")
        vertical_turtle.color("#ff0000")
        vertical_turtle.shape("square")

        horizontal_turtle.backward(25)
        vertical_turtle.backward(50)

        horizontal_turtle.shape(old_shapes[0])
        horizontal_turtle.color(old_colors[0])
        vertical_turtle.shape(old_shapes[1])
        vertical_turtle.color(old_colors[1])

for step in range(50):
  moveTurtles(step*5/3)
  checkColisions()

wn = trtl.Screen()
wn.mainloop()