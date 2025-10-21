#a119_turtle thing
import turtle
from game.player import Player
from util.input import input
from game.EnemyBase import EnemyBase


player : Player = Player(turtle.Turtle())
Input : input = input(player.getScreen())
player.setInput(Input)
enemyTest : EnemyBase = EnemyBase(turtle.Turtle())

while True:
    player.updateMovement()



