#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl


painter = trtl.Turtle()
painter.speed(0)
painter.shape("triangle")
# Add a loop with a zero-iteration condition
start = 'n'
turtle_shapes = painter.screen.getshapes()
i = 0
print(18/4)
while start == 'y':
    painter.begin_fill()
    painter.circle(25, 359)
    painter.end_fill()
    start = input("continue? (y/n) >>> ")
# Add an infinite loop
while turtle_shapes == turtle_shapes:
    if i == len(turtle_shapes):
        i = 0
    painter.shape(turtle_shapes[i])
    i += 1
    painter.screen.delay(100)

wn = trtl.Screen()
wn.mainloop()