import engine
import engine.screen
import engine.runtime
import engine.input

#print(engine.runtime.current_time_millis())
engine.screen.setBackground("blue")
engine.screen.loadTexture("computer-science-class/maze1.png")
engine.screen.update()
engine.runtime.get_physics_thread().add_object(engine.screen.get_test_object())

engine.screen.mainLoop()