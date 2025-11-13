#   a123_apple_1.py
import random
from time import sleep
import time
import turtle as trtl

#-----setup-----
#creating paths and letters
folderPath = "pltw-1.2.3/"
apple_image = f"{folderPath}apple.gif" # Store the file name of your shape
letters = ("abcdefghijklmnopqrstuvwxyz".replace("", " ").strip()).split(" ")
#setting up the screen
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

#creating the dictionary of turtles
turtleList = {0: {}, 1: {}, 2: {}, 3: {}}

#setting up the turtles
wn.tracer(False)
apple = trtl.Turtle()
apple.color("red")
apple.penup()
apple.setpos(-200,0)


apple2 = trtl.Turtle()
apple2.color("green")
apple2.penup()
apple2.setpos(-100,0)

apple3 = trtl.Turtle()
apple3.color("blue")
apple3.penup()
apple3.setpos(100,0)

apple4 = trtl.Turtle()
apple4.color("purple")
apple4.penup()
apple4.setpos(200,0)

apple5 = trtl.Turtle()
apple5.color("yellow")
apple5.penup()
apple5.setpos(0,0)

#adding turtles to the dictionary
turtleList[0] = {"trtl" : apple, "letter": letters.pop(random.randint(0,len(letters)-1))}
turtleList[1] = {"trtl" : apple2, "letter": letters.pop(random.randint(0,len(letters)-1))}
turtleList[2] = {"trtl" : apple3, "letter": letters.pop(random.randint(0,len(letters)-1))}
turtleList[3] = {"trtl" : apple4, "letter": letters.pop(random.randint(0,len(letters)-1))}
turtleList[4] = {"trtl" : apple5, "letter": letters.pop(random.randint(0,len(letters)-1))}

wn.tracer(True)

wn.bgpic(f"{folderPath}background.gif")

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  """Draws the updated apple"""
  active_apple["trtl"].shape(apple_image)
  active_apple["trtl"].penup()
  wn.tracer(False)

  active_apple["trtl"].setpos(active_apple["trtl"].xcor(),0)
  active_apple["trtl"].showturtle()
  active_apple["trtl"].setpos(active_apple["trtl"].xcor()-18, active_apple["trtl"].ycor()-40)
  active_apple["trtl"].write(active_apple["letter"], font=("Arial", 55, "bold"))
  active_apple["trtl"].setpos(active_apple["trtl"].xcor()+18, active_apple["trtl"].ycor()+40)
  wn.tracer(True)
  wn.update()

def make_apple_fall(key):
  """makes apples fall"""
  global turtleList, letters
  #loops through all the turtles to see if any are assigned to the pressed key
  for i in range(len(turtleList)):
    selectedTurtle = turtleList.get(i)
    if selectedTurtle["letter"] == key: # type: ignore
      letters.append(selectedTurtle["letter"])# type: ignore
      selectedTurtle["trtl"].clear() # type: ignore
      selectedTurtle["trtl"].goto(selectedTurtle["trtl"].xcor(), selectedTurtle["trtl"].ycor()-125) # type: ignore
      selectedTurtle["trtl"].hideturtle() # type: ignore
      selectedTurtle["letter"] = letters.pop(random.randint(0,len(letters)-1)) # type: ignore
      draw_apple(selectedTurtle)

    # if(turtle == key):
    #   turtle.clear()
    #   turtle.goto(turtle.xcor(), turtle.ycor()-125)
    #   turtle.hideturtle()
    #   time.sleep(1)
    #   draw_apple(turtle)

  

#-----function calls-----
#key pressed event
wn.getcanvas().master.bind("<KeyPress>", lambda key : make_apple_fall(key.char))
#seting up the first apples
for i in range(len(turtleList)):
  draw_apple(turtleList.get(i))
#other stuff
wn.listen()
wn.mainloop()