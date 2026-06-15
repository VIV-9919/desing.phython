import turtle 
tu=turtle.Turtle() 
tu.screen.bgcolor("black")
tu.pensize(3         )
tu.color("green")
tu.left(80)

tu.backward(80)
tu.speed(160) 
tu.shape("turtle")

def tree(i):
    if i<10:
        return
    else:
        tu.forward(i)
        tu.color("orange")
        tu.circle(2)
        tu.color("brown")
        tu.left(100)
        tree(3*i/4)
        tu.right(30)
        tree(3*i/4)
        tu.backward(i)
tree(70)
turtle.done()