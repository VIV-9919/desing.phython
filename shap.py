import turtle

s = turtle.Screen()
s.bgcolor("black")  # Black background par jyada achcha dikhega

pen = turtle.Turtle()
pen.speed(3)
pen.color("red")
pen.width(5)

pen.begin_fill()
pen.fillcolor("red")

# Left side drawing
pen.left(140)
pen.forward(180)

# Yahan dhyaan dein: 200 degree ghumna zaroori hai
for _ in range(200):
    pen.right(1)
    pen.circle(-90, 1)

pen.left(120)

# Doosra curve
for _ in range(200):
    pen.right(1)
    pen.circle(-90, 1)

pen.forward(180)
pen.end_fill()

# Naam likhne ke liye
pen.up()
pen.goto(0, -50)
pen.down()
pen.color("white")
# 'font' ki spelling sahi rakhein
pen.write("Vivekananda", align="center", font=("Arial", 25, "bold"))

pen.hideturtle()
turtle.done()