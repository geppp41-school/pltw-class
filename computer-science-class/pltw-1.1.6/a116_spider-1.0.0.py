import turtle as trtl

from numpy import dot

spider = trtl.Turtle()
#spider.hideturtle()
spider.speed(0)

#draw body
spider.pensize(60)
spider.circle(30)

#draw head
spider.penup()
spider.goto(0,-60)
spider.pendown()
spider.circle(15)

#draw eyes
for i in range(2):
    spider.penup()
    spider.pensize(30)
    spider.goto(-15 if i == 0 else 15, -75)#sets x to -15 if i is 0 else set it to 15
    spider.color("red")
    spider.pendown()
    spider.dot(15)

for i in range(8):
    spider.penup()
    spider.pensize(5)
    spider.color("black")
    if i % 2 == 0:
        spider.goto(80, -100+(25*(i/2)))
        spider.setheading(55+i*3)
    else:
        spider.goto(-80, -100+(25*(i/3)))
        spider.setheading(360-55-i*2)
        
    spider.pendown()
    spider.circle(75, 100*(-1 if i % 2 != 0 else 1))


wn = trtl.Screen()
wn.mainloop()