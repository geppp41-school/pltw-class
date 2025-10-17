# CODE TO COPY
#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
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
for step in range(50):
  #for each horizontal_turtle
  for turtle in horiz_turtles:
    turtle.speed(step%10)
    #move forward 50 steps
    turtle.forward(50)
    # for each other turtle
    for i in range(len(horiz_turtles)):
      #remove turtles from list if they are too close
      if(horiz_turtles[i] != turtle):
        if turtle.distance(horiz_turtles[i]) <= 20:
          horiz_turtles.remove(horiz_turtles[i])
          horiz_turtles.remove(turtle)
    for i in range(len(vert_turtles)):
      if(vert_turtles[i] != turtle):
        if turtle.distance(vert_turtles[i]) <= 20:
          vert_turtles.remove(vert_turtles[i])
          horiz_turtles.remove(turtle)

  for turtle in vert_turtles:
    turtle.speed(step%10)
    #move forward 50 steps
    turtle.forward(50)
    # for each other turtle
    for i in range(len(horiz_turtles)):
      #remove turtles from list if they are too close
      if(horiz_turtles[i] != turtle):
        if turtle.distance(horiz_turtles[i]) <= 20:
          horiz_turtles.remove(horiz_turtles[i])
          vert_turtles.remove(turtle)
    for i in range(len(vert_turtles)):
      if(vert_turtles[i] != turtle):
        if turtle.distance(vert_turtles[i]) <= 20:
          vert_turtles.remove(vert_turtles[i])
          vert_turtles.remove(turtle)

wn = trtl.Screen()
wn.mainloop()