#a119_turtle thing
import turtle
from game.player import Player
from util.input import input


player : Player = Player(turtle.Turtle())
Input : input = input(player.getScreen())
player.setInput(Input)

while True:
    player.updateMovement()



