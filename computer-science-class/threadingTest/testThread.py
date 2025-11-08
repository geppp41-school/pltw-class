
import threading
import time
from turtle import Turtle


class testThread(threading.Thread):
    def __init__(self, turtle:Turtle):
        super().__init__()
        self.turtle = turtle

    def run(self) -> None:
        for i in range(10):
            self.turtle.forward(50)
            print("moving test")
            time.sleep(1)
