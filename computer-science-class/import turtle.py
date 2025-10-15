import turtle

bob = turtle.Turtle()
bob.speed(10)
bob.pu()
bob.setpos(-150,300)#top of the screen
colors = ["red", "green", "blue"]
selected_color = -1
tower = 0
count = 0
while tower != 3:
    
    if(count % 3 == 0):
        if selected_color == 2:
            selected_color = 0
        else:
            selected_color += 1
    bob.color(colors[selected_color], colors[selected_color])
    bob.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            bob.forward(100)
            bob.right(90)
        else:
            bob.forward(25)
            bob.right(90)
    bob.end_fill()
    count += 1
    if(count == 21):
        count = 0
        tower += 1
        bob.setpos(-150+(100*tower), 300)
    else:
        bob.setpos(-150+(100*tower), bob.ycor() - 25)

turtle.mainloop()