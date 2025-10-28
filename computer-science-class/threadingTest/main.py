import queue
import threading
import turtle
import time

def turtleTask(t:turtle.Turtle):
    for i in range(10):
        t.circle(50)
        print("moving test")
        time.sleep(1)

def process_queue():
    while not graphics.empty():
        (graphics.get())(1)
    
    if threading.active_count() > 1:
        turtle.ontimer(process_queue, 100)

graphics = queue.Queue(1)

turtle1 = turtle.Turtle()
turtle1.right(180)
turtle2 = turtle.Turtle()
test = threading.Thread(target=turtleTask, args=(turtle1, ))
test.daemon = True
test.start()

test2 = threading.Thread(target=turtleTask, args=(turtle2, ))
test2.daemon = True
test2.start()

process_queue()
print("test")

turtle.exitonclick()
