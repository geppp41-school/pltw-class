import random
from sqlite3 import Time
import threading

import time
import turtle
from game.player import Player
from util.input import input
from game.EnemyBase import EnemyBase
from game.Threads.PhysicsThread import PhysicsThread

player : Player = Player(turtle.Turtle())
Input : input = input(player.getScreen())
player.setInput(Input)
enemy = EnemyBase(turtle.Turtle())
enemy.setTargetPlayer(player)
startTime = time.time()
timePassed = startTime-time.time()
endTime = None

backgroundTurtle = turtle.Turtle()
backgroundTurtle.color("Green")
backgroundTurtle.penup()
backgroundTurtle.goto(-400,400)
backgroundTurtle.begin_fill()




while True:
    player.updateMovement()
    enemy.update()
    timePassed = time.time() - startTime
    with player.getScreen().no_animation(): # type: ignore
        backgroundTurtle.clear()
        for i in range(3):
            backgroundTurtle.forward(1200)
            backgroundTurtle.right(90)
        backgroundTurtle.end_fill()
        backgroundTurtle.pendown()
        for i in range(500):
            backgroundTurtle.penup()
            backgroundTurtle.setposition(random.randint(-300, 300), random.randint(-300,300))
            backgroundTurtle.dot(10, "yellow")
    



