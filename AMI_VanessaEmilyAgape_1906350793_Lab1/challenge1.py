import turtle

turtle.hideturtle()
turtle.ht()

turtle.color('yellow')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.penup()
turtle.left(90)
turtle.forward(110)
turtle.right(90)
turtle.forward(50)

turtle.pendown()
turtle.color('black')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.left(180)
turtle.forward(100)
turtle.right(180)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(10)
turtle.left(90)
turtle.setheading(-60)
turtle.pendown()
turtle.circle(70, 120)

