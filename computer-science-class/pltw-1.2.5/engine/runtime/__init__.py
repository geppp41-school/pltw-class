import threading
import time
from typing import Callable
from engine.util.types import TexturedObject, Vector2
import random

def current_time_millis():
    """Returns the current time in milliseconds since the epoch."""
    return int(round(time.time() * 1000))

class __physicsThread(threading.Thread):
    def __init__(self) -> None:
        self.test = None
        super().__init__()
    def run(self):
        while True:
            # Perform periodic runtime tasks here
            if(self.test is not None):
                self.test.transform.Position = Vector2(random.randint(0, 100), random.randint(0, 100))
            time.sleep(1)  # Sleep for a while to avoid busy waiting
    def add_object(self, obj: TexturedObject | None):
        if(obj is not None):
            self.test = obj
physicsThread = __physicsThread()
physicsThread.start()
def get_physics_thread() -> __physicsThread:
    return physicsThread
