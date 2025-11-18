import threading
import time
from typing import Callable


def current_time_millis():
    """Returns the current time in milliseconds since the epoch."""
    return int(round(time.time() * 1000))

class __physicsThread(threading.Thread):
    def __init__(self) -> None:
        super().__init__()
    def run(self):
        while True:
            # Perform periodic runtime tasks here
            time.sleep(1)  # Sleep for a while to avoid busy waiting

