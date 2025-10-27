

import threading
from turtle import Turtle, TurtleScreen
from game.EnemyBase import EnemyBase
import util.Time as time

class PhysicsThread(threading.Thread):
    def __init__(self, screen:TurtleScreen, name="Physics Thread") -> None:
        super().__init__()
        self.__screen = screen
        self._stop_event = threading.Event()
        self._enemies = []

        self._lastUpdateCallTime = time.time_ms()
        self._dt = time.time_ms()-self._lastUpdateCallTime
        pass

    def spawnEnemy(self, Turtle:Turtle):
        self._enemies.append(EnemyBase(Turtle))

    def run(self):
        while not self._stop_event.is_set():
            self._dt = time.time_ms()-self._lastUpdateCallTime
            self._lastUpdateCallTime = time.time_ms()
            for i in range(len(self._enemies)):
                self._enemies[i].update()


    def stop(self):
        self._stop_event.set()

    pass