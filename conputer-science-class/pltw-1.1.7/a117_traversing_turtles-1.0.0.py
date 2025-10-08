#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#  sets up the starting x and y position
startx = 0
starty = 0

#sets the turtles position to startx, starty. makes the turtle turn right 45 degreese and move forward 50 something
for t in my_turtles:
  t.goto(startx, starty)
  t.right(45)     
  t.forward(50)

#increases startx and starty by 50 using var_name = var_name + 50 instead of var_name += 50
  startx = startx + 50
  starty = starty + 50

wn = trtl.Screen()
wn.mainloop()