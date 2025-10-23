import math
import time
from turtle import Turtle, Vec2D, speed
import turtle
from game.player import Player

class EnemyBase:
    def __init__(self, body : Turtle, maxHp : int = 100, speed : float = 1.25, name : str = "", type : str = "", frames : int = 12) -> None:
        self.__body : Turtle = body
        self.__maxHp = maxHp
        self.__hp = maxHp
        self.__speed = speed
        self.__name = name
        self.__type = type
        self.__frameCount = frames
        self.__fps = 12
        self.__frameTime = 12/150
        self.__frames = []
        self.__currentFrame = 0
        self.__lastFrameTime = time.time()/1000
        self.__target = None
        self.__lastFrame = time.time_ns()*1000000
        self.__dt = time.time_ns()*1000000-self.__lastFrame
        #TODO: get the frames of the gif extracted and animate turtle
        for i in range(self.__frameCount):
            self.__body.getscreen().register_shape(f"computer-science-class/pltw-1.1.9/assets/enemies/GreenSlime/sprite_{i}.png")
            self.__frames.append(f"computer-science-class/pltw-1.1.9/assets/enemies/GreenSlime/sprite_{i}.png")

        self.__body.shape("computer-science-class/pltw-1.1.9/assets/enemies/GreenSlime/sprite_0.png")
        pass


    def setTargetPlayer(self, target : Player):
        self.__target = target

    def die(self):
        del self

    def damage(self, damage : float):
        self.__hp -= damage
        pass

    def heal(self, value : float):
        self.__hp = min(self.__hp + value, self.__maxHp)
        pass

    def behavior(self):
        pass

    def update(self):
        self.__dt = time.time_ns()*1000000 - self.__lastFrame
        self.__lastFrame = time.time_ns()
        if(time.time() - self.__lastFrameTime > self.__frameTime):
            self.__body.shape(self.__frames[self.__currentFrame])
            self.__currentFrame = self.__currentFrame + 1 if self.__currentFrame+1 < self.__frameCount else 0
            self.__lastFrameTime = time.time()

        if(self.__target != None):
            
            angle = self.__body.towards(self.__target.getPos())
            self.__body.setheading(angle)
            direction = Vec2D.rotate(Vec2D(1,1), angle)
            print(direction)
            velocity = direction * self.__speed
            self.__body.setpos(self.__body.pos() + (velocity*self.__dt))
            self.__body.teleport()
            pass

        pass
