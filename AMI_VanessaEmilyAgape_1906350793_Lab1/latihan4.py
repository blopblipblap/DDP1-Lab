import turtle
import math
nama=input("Masukkan nama pengguna: ")
if (nama=="Pak Chanek"):
    turtle.circle(100)
else:
    turtle.forward(100)

    turtle.left(90)
    turtle.forward(100)

    turtle.left(180-45)
    turtle.forward(100*math.sqrt(2))

    turtle.exitonclick()
    turtle.mainloop()
