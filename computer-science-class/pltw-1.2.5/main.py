import engine
import engine.screen
import engine.runtime

#print(engine.runtime.current_time_millis())
engine.screen.setBackground("blue")
engine.screen.loadTexture("computer-science-class/maze1.png")
engine.screen.update()

engine.screen.mainLoop()