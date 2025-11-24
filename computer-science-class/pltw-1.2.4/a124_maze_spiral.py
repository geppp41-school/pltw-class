import random
import turtle

maze_size = "12x12"
maze_start = turtle.Vec2D(0, 0)
maze_end = turtle.Vec2D(9, 9)
maze = []

mazeGenerator = turtle.Turtle()
mazeGenerator.shape("square")

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


        
        
    
    turtle.tracer(True)

draw_base_maze()

def get_possible_directions(x,y):
    possible_directions = "nesw"
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
        if(maze[x][y-1]["visited"] == True): # type: ignore
            possible_directions = possible_directions.replace("n", "x")

    if (possible_directions.find("e") != -1):
        if(maze[x+1][y]["visited"] == True): # type: ignore
            possible_directions = possible_directions.replace("e", "x")
        
    if (possible_directions.find("s") != -1):
        if(maze[x][y+1]["visited"] == True): # type: ignore
            possible_directions = possible_directions.replace("s", "x")
        
    
    if (possible_directions.find("w") != -1):
        if(maze[x-1][y]["visited"] == True): # type: ignore
            possible_directions = possible_directions.replace("w", "x")
    return possible_directions

def draw_maze(x,y):
    maze[x][y]["visited"] = True
    while(get_possible_directions(x,y) != "xxxx"):
        mazeGenerator.goto((x*20)+10,(y*(-20))-10)
        mazeGenerator.dot(5)
        turtle.tracer(True)
        possible_directions = get_possible_directions(x,y).replace("x", "")
        
        
        direction = random.choice(possible_directions)
        # TODO: simplify this by moving all the movement stuff apart from set heading to another functino
        if(direction == "n"):
            mazeGenerator.setheading(90)
            mazeGenerator.forward(10)
            mazeGenerator.pencolor("white")
            mazeGenerator.dot(19)
            mazeGenerator.pencolor("black")
            mazeGenerator.forward(10)
            draw_maze(x, y-1)
            maze[x][y]["connections"] = "n" + maze[x][y]["connections"][1] + maze[x][y]["connections"][2] + maze[x][y]["connections"][3]
            pass
        elif(direction == "e"):
            mazeGenerator.setheading(0)
            mazeGenerator.forward(10)
            mazeGenerator.pencolor("white")
            mazeGenerator.dot(19)
            mazeGenerator.pencolor("black")
            mazeGenerator.forward(10)
            draw_maze(x+1, y)
            maze[x][y]["connections"] = maze[x][y]["connections"][0] + "e" + maze[x][y]["connections"][2] + maze[x][y]["connections"][3]
            pass
        elif(direction == "s"):
            mazeGenerator.setheading(270)
            mazeGenerator.forward(10)
            mazeGenerator.pencolor("white")
            mazeGenerator.dot(19)
            mazeGenerator.pencolor("black")
            mazeGenerator.forward(10)
            draw_maze(x, y+1)
            maze[x][y]["connections"] = maze[x][y]["connections"][0] + maze[x][y]["connections"][1] + "s" + maze[x][y]["connections"][3]
            pass
        elif(direction == "w"):
            mazeGenerator.setheading(180)
            mazeGenerator.forward(10)
            mazeGenerator.pencolor("white")
            mazeGenerator.dot(19)
            mazeGenerator.pencolor("black")
            mazeGenerator.forward(10)
            draw_maze(x-1, y)
            maze[x][y]["connections"] = maze[x][y]["connections"][0] + maze[x][y]["connections"][1] + maze[x][y]["connections"][2] + "w"
            pass
        turtle.tracer(False)
        

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
mazeGenerator.hideturtle()
turtle.mainloop()
