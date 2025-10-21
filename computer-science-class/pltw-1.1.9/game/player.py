import turtle

from util.input import *
from util.Vector import *

class Player:
    def __init__(self, Turtle : turtle.Turtle):
        self.__speed : float = 1.0
        self.__turtle : turtle.Turtle = Turtle
        pass

    def getScreen(self):
        return self.__turtle.getscreen()
    
    def setInput(self, Input : input):
        self.__input = Input
        pass

    def updateMovement(self):
        turtlePosition = self.__turtle.pos()
        
        turtleMovement = Vector2D(
            self.__input.isKeyPressedInt("w")-self.__input.isKeyPressedInt("s"),
            self.__input.isKeyPressedInt("d")-self.__input.isKeyPressedInt("a")
        )
        turtleMovement = turtleMovement.normalized()
        print("3" + str(turtleMovement))
        self.__turtle.setpos(
            turtlePosition[0]+turtleMovement[1],
            turtlePosition[1]+turtleMovement[0]
        )
        
    def mainLoop(self):
        self.__turtle.screen.mainloop()

    

    