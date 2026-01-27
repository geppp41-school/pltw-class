import random
import turtle

maze_size = "15x15"

maze = []

mazeGenerator = turtle.Turtle()
mazeGenerator.shape("square")

exitTurtle = turtle.Turtle()
exitTurtle.hideturtle()
exitTurtle.shape("square")
exitTurtle.color("red")
exitTurtle.shapesize(0.5)
exitTurtle.penup()

player = turtle.Turtle()
player.hideturtle()
player.penup()
player.setpos(10,-10)
player.speed(0)
playerPosition = turtle.Vec2D(0,0)
#setup the maze array

def create_maze_array():
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
            maze[x][y-1]["connections"] = maze[x][y-1]["connections"][0] + maze[x][y-1]["connections"][1] + "s" + maze[x][y-1]["connections"][3]
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
            maze[x+1][y]["connections"] = maze[x+1][y]["connections"][0] + maze[x+1][y]["connections"][1] + maze[x+1][y]["connections"][2] + "w"
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
            maze[x][y+1]["connections"] = "n" + maze[x][y+1]["connections"][1] + maze[x][y+1]["connections"][2] + maze[x][y+1]["connections"][3]
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
            maze[x-1][y]["connections"] = maze[x-1][y]["connections"][0] + "e" + maze[x-1][y]["connections"][2] + maze[x-1][y]["connections"][3]
            draw_maze(x-1, y)
            maze[x][y]["connections"] = maze[x][y]["connections"][0] + maze[x][y]["connections"][1] + maze[x][y]["connections"][2] + "w"
            pass
        
def add_exit():
    x = int(maze_size.split("x")[0])
    y = int(maze_size.split("x")[1])
    exitTurtle.goto((random.randint(0, x-1)*20)+10, (random.randint(0, y-1)*-20)-10)
    exitTurtle.showturtle()

def moveUp():
    global playerPosition
    turtle.tracer(False)
    if(maze[playerPosition[0]][playerPosition[1]]["connections"].find("n") != -1): # type: ignore
        player.setheading(90)
        playerPosition = turtle.Vec2D(playerPosition[0], playerPosition[1] - 1) 
        player.setposition((playerPosition[0]*20)+10, (playerPosition[1]*-20)-10)
        pass
    turtle.tracer(True)
    pass

def moveLeft():
    global playerPosition
    turtle.tracer(False)
    if(maze[playerPosition[0]][playerPosition[1]]["connections"].find("w") != -1): # type: ignore
        player.setheading(180)
        playerPosition = turtle.Vec2D(playerPosition[0]-1, playerPosition[1]) 
        player.setposition((playerPosition[0]*20)+10, (playerPosition[1]*-20)-10)
        pass
    turtle.tracer(True)
    pass

def moveRight():
    global playerPosition
    turtle.tracer(False)
    if(maze[playerPosition[0]][playerPosition[1]]["connections"].find("e") != -1): # type: ignore
        player.setheading(0)
        playerPosition = turtle.Vec2D(playerPosition[0]+1, playerPosition[1]) 
        player.setposition((playerPosition[0]*20)+10, (playerPosition[1]*-20)-10)
        pass
    turtle.tracer(True)
    pass

def moveDown():
    global playerPosition
    turtle.tracer(False)
    if(maze[playerPosition[0]][playerPosition[1]]["connections"].find("s") != -1): # type: ignore
        player.setheading(270)
        playerPosition = turtle.Vec2D(playerPosition[0], playerPosition[1] + 1) 
        player.setposition((playerPosition[0]*20)+10, (playerPosition[1]*-20)-10)
        pass
    turtle.tracer(True)
    pass


#turtle.tracer(False)
create_maze_array()
draw_maze(0,0)
add_exit()
#turtle.tracer(True)


player.getscreen().onkeypress(moveUp, "w")
player.getscreen().onkeypress(moveLeft, "a")
player.getscreen().onkeypress(moveDown, "s")
player.getscreen().onkeypress(moveRight, "d")
player.getscreen().listen()
player.showturtle()


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
while (exitTurtle.distance(player) != 0):
    exitTurtle.color("red")
player.getscreen().onkeypress(None, "w") # type: ignore
player.getscreen().onkeypress(None, "a")# type: ignore
player.getscreen().onkeypress(None, "s")# type: ignore
player.getscreen().onkeypress(None, "d")# type: ignore
player.getscreen().listen()
exitTurtle.color("green")
exitTurtle.write("You Win!", align="center", font=("Arial", 16, "normal"))
turtle.mainloop()
