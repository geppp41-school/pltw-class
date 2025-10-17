#   a114_while_guess.py

import turtle as trtl
import math
from random import randint

# modify with your two favorite colors
color1 = "orange"
color2 = "purple"

wn = trtl.Screen()
height = wn.screensize()[1] # the radius of the shape
wn.screensize(1920, 1080)

wn.colormode(255)
painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

space = 1
angle =  75# experiment with the shape
seg = int(360/angle)

def move(turtle: trtl.Turtle):
  turtle.right(angle)
  turtle.forward(2*space + 10)
  turtle.begin_fill()
  turtle.circle(3)
  turtle.end_fill()

while (painter.ycor() < height):
  print()
  print(painter.pos())
  if space % 5 == 0:
    painter.color((randint(0,255), randint(0,255), randint(0,255)))


  move(painter)
  space += 1

  #print(space%5)


wn.mainloop()