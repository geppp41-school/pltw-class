
from narwhals import String
from typing_extensions import Self
from turtle import Turtle

class Animation:
    def __new__(cls, Turtle:Turtle, type:String) -> Self:
        ##TODO: use json files for configuring animation data 
        
        return super(Animation, cls).__new__(cls)
    
    def __init__(self) -> None:

        pass
    pass