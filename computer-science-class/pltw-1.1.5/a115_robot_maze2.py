#   a115_robot_maze.py
from itertools import count
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()


wn.bgpic("maze2.png")

#robot movement
def forward(count = 1):
  for i in range(count):
    move()
def right(count = 1):
  for i in range(count):
    for x in range(3):
      turn_left()
def left(count = 1):
  for i in range(count):
    turn_left()


for iteration in range(2):
  match iteration:
    case 0:
      forward(3)
      right()
      forward(2)
      robot.dot(10)
    case 1:
      robot.goto(startx,starty)
      robot.setheading(90)
      robot.color("purple")
      right()
      for i in range(2):
        forward(3)
        left()
      forward()

#---- end robot movement 

wn.mainloop()
