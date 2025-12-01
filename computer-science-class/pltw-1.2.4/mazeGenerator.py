
import turtle


__turtle: turtle.Turtle
__maze_size = None
__maze = []

def set_turtle(turtle_instance):
    global __turtle
    __turtle = turtle_instance

def set_maze_size(size):
    global __maze_size
    __maze_size = size

def __generate_empty_maze():
    global __maze
    if(__maze_size is None):
        raise Exception("Maze size not set")
    size_x = int(__maze_size.split("x")[0])
    size_y = int(__maze_size.split("x")[1])
    for x in range(size_x):
        __maze.append([])
        for y in range(size_y):
            __maze[x].append({"connections": "xxxx", "visited": False})

def draw_base_maze():
    global __turtle
    global __maze_size
    mazeGenerator: turtle.Turtle = __turtle
    x_size = int(__maze_size.split('x')[0]) # type: ignore
    y_size = int(__maze_size.split('x')[1]) # type: ignore
    #draw border
    for i in range(2):
        mazeGenerator.forward(x_size*20)
        mazeGenerator.right(90)
        mazeGenerator.forward(y_size*20)
        mazeGenerator.right(90)
    
    #draw collums
    for i in range(x_size-1):
        mazeGenerator.forward(20)
        mazeGenerator.right(90)
        mazeGenerator.forward(y_size*20)
        mazeGenerator.backward(y_size*20)
        mazeGenerator.left(90)

    mazeGenerator.backward((x_size-1)*20)

    #draw rows
    for i in range(y_size-1):
        mazeGenerator.right(90)
        mazeGenerator.forward(20)
        mazeGenerator.left(90)
        mazeGenerator.forward(x_size*20)
        mazeGenerator.backward(x_size*20)
    mazeGenerator.penup()
    mazeGenerator.left(90)
    mazeGenerator.forward((y_size-1)*20-10)
    mazeGenerator.right(90)
    mazeGenerator.forward(10)

def draw_maze(xOffset: int, yOffset: int):
    global __turtle
    global __maze
    mazeGenerator = __turtle
    