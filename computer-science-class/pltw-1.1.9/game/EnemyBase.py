import math
import random
import time
from turtle import Turtle
from util import Vector2
from game.player import Player

class EnemyBase:
    def __init__(self, body : Turtle, maxHp : int = 100, speed : float = 50, name : str = "", type : str = "", frames : int = 12) -> None:
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
        self.__lastFrame = time.time_ns()/1000000000
        self.__dt = time.time_ns()/1000000000-self.__lastFrame
        self.__tryWindowsDirs = False
        
        #TODO: get the frames of the gif extracted and animate turtle
        for i in range(self.__frameCount):
            try:
                self.__body.getscreen().register_shape(f"computer-science-class/pltw-1.1.9/assets/enemies/GreenSlime/sprite_{i}.png")
                self.__frames.append(f"computer-science-class/pltw-1.1.9/assets/enemies/GreenSlime/sprite_{i}.png")  
            except:
                self.__body.getscreen().register_shape(f"pltw-1.1.9\\assets\\enemies\\GreenSlime\\sprite_{i}.png")
                self.__frames.append(f"pltw-1.1.9\\assets\\enemies\\GreenSlime\\sprite_{i}.png")  
                self.__tryWindowsDirs = True
                
            
        if not self.__tryWindowsDirs:
            self.__body.shape("computer-science-class/pltw-1.1.9/assets/enemies/GreenSlime/sprite_0.png")
        else:
            self.__body.shape(f"pltw-1.1.9\\assets\\enemies\\GreenSlime\\sprite_0.png")

        self.__body.penup()
        self.__body.setpos(random.randint(-250, 250), random.randint(-250,250))
        self.__body.pendown()
        


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
        self.__dt = time.time_ns()/1000000000 - self.__lastFrame
        self.__lastFrame = time.time_ns()/1000000000
        if(time.time() - self.__lastFrameTime > self.__frameTime):
            self.__body.shape(self.__frames[self.__currentFrame])
            self.__currentFrame = self.__currentFrame + 1 if self.__currentFrame+1 < self.__frameCount else 0
            self.__lastFrameTime = time.time()
        screen = self.__body.getscreen()
        with screen.no_animation(): # type: ignore

            if(self.__target != None):
                
                angle = self.__body.towards(self.__target.getPos())
                direction = Vector2.RIGHT.rotated(angle)
                velocity = direction * self.__speed
                self.__body.setpos(self.__body.pos() + (velocity.toVec2D()*self.__dt))
                
                # self.__body.teleport(self.__body.pos()[0] + (velocity.x*self.__dt), self.__body.pos()[1] + (velocity.y*self.__dt))
                # print("done moving")
