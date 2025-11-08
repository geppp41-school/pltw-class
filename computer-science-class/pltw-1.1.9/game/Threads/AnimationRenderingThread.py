import threading
from turtle import TurtleScreen
import util.Time as time

class AnimationRenderingThread(threading.Thread):
    def __init__(self, screen:TurtleScreen, name="Rendering Thread") -> None:
        super().__init__()
        self.name = name
        self.__screen = screen
        self._stop_event = threading.Event()





        self._lastUpdateCallTime = time.time_ms()
        self._dt = time.time_ms()-self._lastUpdateCallTime #delta time aka time between frames / calls    use time.time_ns()/1,000,000,000


    def run(self):
        while not self._stop_event.is_set():
            self._dt = time.time_ms()-self._lastUpdateCallTime
            self._lastUpdateCallTime = time.time_ms()

            with self.__screen.no_animation(): # pyright: ignore[reportAttributeAccessIssue]
                for turtle in self.__screen.turtles():
                    pass
                pass
            

            pass
        pass

    def stop(self):
        self._stop_event.set()
        pass



# import threading
# import time

# class PersistentThread(threading.Thread):
#     def __init__(self, name="PersistentThread"):
#         super().__init__()
#         self.name = name
#         self._stop_event = threading.Event()

#     def run(self):
#         print(f"{self.name} started.")
#         while not self._stop_event.is_set():
#             # Perform persistent task here
#             print(f"{self.name} is doing work...")
#             time.sleep(1) # Simulate work

#         print(f"{self.name} stopped.")

#     def stop(self):
#         self._stop_event.set()

# # Create and start the persistent thread
# my_thread = PersistentThread("MyBackgroundTask")
# my_thread.start()

# # Let the main thread run for a while
# time.sleep(5)

# # Signal the persistent thread to stop
# print("Main thread signaling background thread to stop.")
# my_thread.stop()
# my_thread.join() # Wait for the background thread to finish

# print("Main thread finished.")