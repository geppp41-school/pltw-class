# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import random


#-----game configuration----
playerShape = "square"
shapeFillColor = "blue"
shapeSize = 1
score = 0

font_setup = ("Arial", 20, "normal")

timer = 5
counter_interval = 1000
timer_up = False



#-----initialize turtle-----
player = turtle.Turtle()
player.shape(playerShape)
player.fillcolor(shapeFillColor)
player.shapesize(shapeSize)
player.penup()

score_writer = turtle.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(-310, 270)

counter = turtle.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(-310, 240)


#-----game functions--------
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


def update_score():
    """updates the score counter"""
    global score 
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    pass

def change_position():
    """moves the turtle to a random position"""
    player.goto((random.randint(-200, 200), random.randint(-150, 150)))
    update_score()
    pass

def click(x:float|int, y:float|int):
    """method that gets called when clicking on the player turtle"""
    if timer_up is False:
        change_position()
    else:
       player.hideturtle()
    pass


#-----events----------------
window = turtle.Screen()

player.onclick(click)
window.ontimer(countdown, counter_interval)
window.mainloop()