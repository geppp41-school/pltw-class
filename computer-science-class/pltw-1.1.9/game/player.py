import turtle

from util.input import *
from util.Vector2 import *
from util.Time import *
class Player:
    def __init__(self, Turtle : turtle.Turtle):
        self.__speed : float = 160
        self.__turtle : turtle.Turtle = Turtle
        self.__lastTime = time_ms()
        self.__deltaTime = time_ms()-self.__lastTime
        pass

    def getScreen(self):
        return self.__turtle.getscreen()
    
    def setInput(self, Input : input):
        self.__input = Input
        pass

    def updateMovement(self):
        self.__deltaTime = time_ms() - self.__lastTime
        self.__lastTime = time_ms()
        turtlePosition = self.__turtle.pos()
        
        turtleMovement = Vector2(
            self.__input.isKeyPressedInt("w")-self.__input.isKeyPressedInt("s"),
            self.__input.isKeyPressedInt("d")-self.__input.isKeyPressedInt("a")
        )

        turtleMovement = turtleMovement.normalized()
        turtleMovement *= self.__speed*self.__deltaTime
        self.__turtle.setpos(
            turtlePosition[0]+turtleMovement[1],
            turtlePosition[1]+turtleMovement[0]
        )
        
    def mainLoop(self):
        self.__turtle.screen.mainloop()

    def getHeading(self):
        return self.__turtle.heading()
    
    def getPos(self):
        return self.__turtle.pos()
    

    