

import threading
from turtle import Turtle, TurtleScreen
from game.EnemyBase import EnemyBase
import util.Time as time

class PhysicsThread(threading.Thread):
    def __init__(self, screen:TurtleScreen, lock, name="Physics Thread") -> None:
        super().__init__()
        for thread in threading.enumerate():
            print(thread.name)
        self.__screen = screen
        self._stop_event = threading.Event()
        self._enemies = []
        self._lock = lock

        self._lastUpdateCallTime = time.time_ms()
        self._dt = time.time_ms()-self._lastUpdateCallTime
        self.__screen.tracer()
        pass

    def spawnEnemy(self, Turtle:Turtle):
        with self.__screen.no_animation(): # type: ignore 
            self._enemies.append(EnemyBase(Turtle))

    def run(self):
        #self.__screen.cv.after(100, self.__update)
        for enemy in self._enemies:
            enemy.update()
        print("test")
            
    def __update(self, *args):
        self._dt = time.time_ms()-self._lastUpdateCallTime
        self._lastUpdateCallTime = time.time_ms()
        for i in range(len(self._enemies)):
            self._enemies[i].update()
        self.__screen.update()

    def stop(self):
        self._stop_event.set()

    pass