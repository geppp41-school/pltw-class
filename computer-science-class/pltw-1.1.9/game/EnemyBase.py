import time
from turtle import Turtle
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
        self.__msPerFrame = self.__fps / 1000
        self.__frames = {}
        self.__currentFrame = 0
        self.__lastFrameTime = time.time()
        #TODO: get the frames of the gif extracted and animate turtle

        self.__body.getscreen().register_shape("computer-science-class/pltw-1.1.9/assets/enemies/GreenSlime/slime_10.png")
        self.__body.shape("computer-science-class/pltw-1.1.9/assets/enemies/GreenSlime/slime_10.png")
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
