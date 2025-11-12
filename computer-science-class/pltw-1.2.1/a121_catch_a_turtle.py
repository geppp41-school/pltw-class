# a121_catch_a_turtle.py
#-----import statements-----
import json
import os
import sys
import turtle
import random


#-----game configuration----
#seting up file paths
_scoreFilePathLynx = "computer-science-class/pltw-1.2.1/highScores.json"
_scoreFIlePathWin = "computer-science-class\\pltw-1.2.1\\highScores.json"
#stuff for the player
playerShape = "square"
shapeFillColor = "blue"
shapeSize = 1
score = 0
name = ""

#high scores
HighScores:list = []

#font
font_setup = ("Arial", 20, "normal")

#timer
timer = 10
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

leaderboard_writer = turtle.Turtle()
leaderboard_writer.penup()
leaderboard_writer.hideturtle()


#--------file stuff---------
def read_high_score_file():
    """read the file containing the high scores"""
    global HighScores
    if (sys.platform == "linux"):
       with open(_scoreFilePathLynx, "r") as scoreFile:
          jsonObject:dict = json.load(scoreFile)
          
          HighScores = jsonObject.get("scores", [])
          print(HighScores)
          scoreFile.close()
    elif(sys.platform == "win32"):
       with open(_scoreFIlePathWin, "r") as scoreFile:
          jsonObject:dict = json.load(scoreFile)
          
          HighScores = jsonObject.get("scores", [])
          print(HighScores)
          scoreFile.close()

def write_high_score_file():
   """write the updated high scores to the file"""
   if (sys.platform == "linux"):
       with open(_scoreFilePathLynx, "w") as scoreFile:
          json.dump({"scores": HighScores}, scoreFile)
          scoreFile.close()
   elif(sys.platform == "win32"):
       with open(_scoreFIlePathWin, "w") as scoreFile:
           json.dump({"scores": HighScores}, scoreFile)
           scoreFile.close()

#-----game functions--------
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    #show that the time is up
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    update_leaderboard()
  else:
    #updates the timers counter
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

def update_leaderboard():
   player.hideturtle()
   #sorting the scores
   for i in range(5):
      score1 = HighScores[i]
      score2 = HighScores[4]
      if(score2.get("score") > score1.get("score")):
         HighScores[i] = score2
         HighScores[4] = score1
    
    #checking player score against leaderboard
   for i in range(5):
        if(score > HighScores[i].get("score")):
           HighScores.pop(4)
           HighScores.insert(i, {"name": name, "score": score})
           break
        
   write_high_score_file()#saving the updated scores
   #creating the output
   for i in range(5):
      if(i == 0):
         leaderboard_writer.color("#e1eb34")#gold
      elif(i == 1):
         leaderboard_writer.color("#cfcdca")#silver
      elif(i == 2):
         leaderboard_writer.color("#9c6110")#bronze
      else:
         leaderboard_writer.color("#000000")#normal color
      #displays the leaderboard
      leaderboard_writer.write(f"{HighScores[i].get("name")}: {HighScores[i].get("score")}\n", font=font_setup)
      leaderboard_writerPos = leaderboard_writer.position()
      leaderboard_writer.setposition(leaderboard_writerPos[0], leaderboard_writerPos[1]-30)
      

   

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
window = player.getscreen()
read_high_score_file()    
print("please enter a name")
name = input(">>> ")


player.onclick(click)
window.ontimer(countdown, counter_interval)
window.mainloop()