import math
from turtle import Vec2D, right
from typing import overload



class Vector2:
    
    def __new__(cls, x, y):
        return super(Vector2, cls).__new__(cls)
    
    def __init__(self, x : float, y : float) -> None:
        self.x = x
        self.y = y

    def __getitem__(self, index: int):
        if(index > 1 or index < 0):
            raise IndexError("Index is out of bounds")
        else:
            return self.x if index == 0 else self.y
    
    def __setitem__(self, index : int, value: float):
        if(index > 1 or index < 0):
            raise IndexError("Index is out of bounds")
        elif(index == 0):
            self.x = value
        else:
            self.y = value

    def normalized(self):
        return Vector2(
            self.x / math.sqrt(self.x*self.x+self.y*self.y) if self.x != 0 else 0,
            self.y / math.sqrt(self.x*self.x+self.y*self.y) if self.y != 0 else 0
        ) 
    
    def rotated(self, deg):
        deg = math.radians(deg)
        return Vector2(
            self.x*math.cos(deg) - self.y*math.sin(deg),
            self.x*math.sin(deg) - self.y*math.cos(deg)
        )
    
    def __mul__(self, val : float):
        self.x = self.x*val
        self.y = self.y*val
        return self
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    
    def toVec2D(self) -> Vec2D:
        return Vec2D(self.x, self.y)
    

RIGHT = Vector2(1,0)
LEFT = Vector2(-1, 0)
UP = Vector2(0, 1)
DOWN = Vector2(0, -1)