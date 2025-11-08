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






while True:
    player.updateMovement()
    enemy.update()
    timePassed = time.time() - startTime
    



