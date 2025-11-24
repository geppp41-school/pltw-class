import random
import turtle

maze_size = "10x10"
maze_start = turtle.Vec2D(0, 0)
maze_end = turtle.Vec2D(9, 9)
maze = []

player = turtle.Turtle()
player.shape("square")

#setup the maze array
for i in range(int(maze_size.split('x')[0])):
    maze.append([])
    for j in range(int(maze_size.split('x')[1])):
        maze[i].append({"connections": "xxxx", "visited": False})



def draw_base_maze():
    turtle.tracer(False)
    x_size = int(maze_size.split('x')[0])
    y_size = int(maze_size.split('x')[1])
    #draw border
    for i in range(2):
        player.forward(x_size*20)
        player.right(90)
        player.forward(y_size*20)
        player.right(90)
    
    #draw collums
    for i in range(x_size-1):
        player.forward(20)
        player.right(90)
        player.forward(y_size*20)
        player.backward(y_size*20)
        player.left(90)

    player.backward((x_size-1)*20)

    #draw rows
    for i in range(y_size-1):
        player.right(90)
        player.forward(20)
        player.left(90)
        player.forward(x_size*20)
        player.backward(x_size*20)
    player.penup()
    player.left(90)
    player.forward((y_size-1)*20-10)
    player.right(90)
    player.forward(10)


        
        
    
    turtle.tracer(True)

draw_base_maze()

def draw_maze(x,y):
    possible_directions = "nesw"
    maze[x][y]["visited"] = True
    #prevent index out of bound errors while checking possible moves
    if(x == 0):
        possible_directions = possible_directions.replace("w", "x")
    elif(x == int(maze_size.split('x')[0])-1):
        possible_directions = possible_directions.replace("e", "x")
    if(y == 0):
        possible_directions = possible_directions.replace("n", "x")
    elif(y == int(maze_size.split('x')[1])-1):
        possible_directions = possible_directions.replace("s", "x")

    #filters out visited cells
    if (possible_directions.find("n") != -1):
        if(maze[x][y+1]["visited"] == True): # type: ignore
            possible_directions = possible_directions.replace("n", "x")

    if (possible_directions.find("e") != -1):
        if(maze[x+1][y]["visited"] == True): # type: ignore
            possible_directions = possible_directions.replace("e", "x")
        
    if (possible_directions.find("s") != -1):
        if(maze[x][y-1]["visited"] == True): # type: ignore
            possible_directions = possible_directions.replace("n", "x")
        
    
    if (possible_directions.find("w") != -1):
        if(maze[x-1][y]["visited"] == True): # type: ignore
            possible_directions = possible_directions.replace("w", "x")

    if(possible_directions != "____"):
        possible_directions = possible_directions.replace("_", "").replace("", " ").split(" ")
    else:
        return 0
    
    direction = random.choice(possible_directions)
    # TODO: simplify this by moving all the movement stuff apart from set heading to another functino
    if(direction == "n"):
        player.setheading(90)
        player.forward(10)
        player.pencolor("white")
        player.dot(19)
        player.pencolor("black")
        player.forward(10)
        draw_maze(x, y+1)
        pass
    elif(direction == "e"):
        player.setheading(0)
        player.forward(10)
        player.pencolor("white")
        player.dot(19)
        player.pencolor("black")
        player.forward(10)
        draw_maze(x+1, y)
        pass
    elif(direction == "s"):
        player.setheading(270)
        player.forward(10)
        player.pencolor("white")
        player.dot(19)
        player.pencolor("black")
        player.forward(10)
        draw_maze(x, y-1)
        pass
    elif(direction == "w"):
        player.setheading(180)
        player.forward(10)
        player.pencolor("white")
        player.dot(19)
        player.pencolor("black")
        player.forward(10)
        draw_maze(x-1, y)
        pass

turtle.tracer(False)
draw_maze(0,0)
turtle.tracer(True)
# this will clear a wall 
# player.forward(10)
# player.pencolor("white")
# player.dot(19)
# player.pencolor("black")
# player.forward(20)


# give a current cell as a parameter
# mark the current cell as visited
# while the current cell has any unvisited neightbor cells
#   choose one of the unvisited neighbor cells
#   remove the wall between the current cell and the neighbors
#   invoke the routine recursively for the chosen cell
#this is the dfs maze generation
player.hideturtle()
turtle.mainloop()
