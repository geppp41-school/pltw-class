#   a115_robot_maze.py
from os import path
import turtle as trtl
from PIL import Image
from numpy import size

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
maze_w , maze_h = [255, 256]

startx = -100
starty = -100
robotpos = [0,4]
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

#settings up maze
print("maze options \n1. maze1\n2. maze2\n3. maze3")
maze = f"maze{input("What maze do you want to use: >>> ")}.png"
image = Image.open(maze)

wn.bgpic(maze) # other file names should be maze2.png, maze3.png


#setting up map
Map = [[],[],[],[],[]]#free sapce is 2 end is >= 25 blocked is 1
end_points = []#list of the found endpoints
for x in range(5):
  for y in range(5):
    Map[x].append(#adds the pixel data of a tile to the map
      image.getpixel([
        round((maze_w/5)/2+x*(maze_w/5)),#image is for some reason 255,256 so i get to add some math
        round((maze_h/5)/2+y*(maze_h/5))
      ])
    )
    if Map[x][y] >= 25:##if the current square has a value >= 25 then its an end point
      end_points.append([x,y])


path = []

x,y = robotpos
for i in range(len(end_points)):
  path_finished = False
  while not path_finished:
    if (end_points[i])[1] < y:
        if(Map[x][y-1] != 1):
          path.append("forward")
          y-=1
        else:
          path.append("right")
          x+=1
    else: 
      path.append("right")
      x+=1
    path_finished = True if end_points[i] == [x,y] else False
  path.append("change-color")

for i in range(len(path)):
  if(path[i] == "forward"):
    while(round(robot.heading()) != 90 ):
      turn_left()
    move()
  elif(path[i] == "right"):
    while(round(robot.heading()) != 0):
      turn_left()
    move()
  elif(path[i] == "change-color"):
    robot.color("red")

for i in range(len(path)):
  match path[i]:
    case "up":
      pass
    case "down":
      pass
    case "left":
      pass
    case "right":
      pass
    case "reset":
      pass
    case "change-color":
      robot.color("red")




#---- end robot movement 

wn.mainloop()
