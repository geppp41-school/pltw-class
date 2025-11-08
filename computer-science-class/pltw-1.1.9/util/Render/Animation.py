
import string
from typing_extensions import Self  # type: ignore
from turtle import Turtle

class Animation:
    def __new__(cls, Turtle:Turtle, type:str) -> Self:
        ##TODO: use json files for configuring animation data 
        
        return super(Animation, cls).__new__(cls)
    
    def __init__(self, Turtle:Turtle, type:str) -> None:
        

        pass
    pass
