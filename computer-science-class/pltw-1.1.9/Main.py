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
physicsThread = PhysicsThread(turtle.Screen(), threading.Lock())


physicsThread.spawnEnemy(turtle.Turtle())

physicsThread.start()
physicsThread.join()
while True:
    player.updateMovement()



