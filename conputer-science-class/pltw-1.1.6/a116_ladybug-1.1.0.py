# CODE TO COPY
#   a116_ladybug.py
from math import cos, pi, sin
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

#legs
ladybug.color("black")
#draw legs 2 and 4
ladybug.penup()
ladybug.pensize(5)
ladybug.goto(-50,-34)
ladybug.pendown()
ladybug.forward(100)

#draw legs 6 and 3
ladybug.penup()
ladybug.goto(-40, -5)
ladybug.pendown()
ladybug.setheading(320)
ladybug.forward(100)

#draw legs 1 and 2
ladybug.penup()
ladybug.goto(-40, -63)
ladybug.pendown()
ladybug.setheading(35)
ladybug.forward(100)

# and body
ladybug.setheading(0)
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()