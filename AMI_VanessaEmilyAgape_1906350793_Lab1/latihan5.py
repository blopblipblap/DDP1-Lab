import turtle
rasa=input("Masukkan rasa donat: ")
if (rasa=="Cokelat"):
    turtle.hideturtle()
    turtle.ht()
    turtle.color("brown")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

    turtle.penup()
    turtle.left(90)
    turtle.forward(50)

    turtle.color("white")
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(90)
    turtle.circle(50)
    turtle.end_fill()

    turtle.penup()

    turtle.exitonclick()
    turtle.mainloop()
elif (rasa=="Stroberi"):
    turtle.hideturtle()
    turtle.ht()
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

    turtle.penup()
    turtle.left(90)
    turtle.forward(50)

    turtle.color("white")
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(90)
    turtle.circle(50)
    turtle.end_fill()

    turtle.penup()

    turtle.exitonclick()
    turtle.mainloop()
else:
    print("Maaf", rasa, "tidak ada di pilihan rasa")
