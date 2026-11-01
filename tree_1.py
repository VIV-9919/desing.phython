from turtle import *    
from colorsys import *
 
tracer(0)
bgcolor("yellow")
h=0  
goto(0, 0)
for i in range(70):
    color(hsv_to_rgb(h, 1, 1))
    h+=0.02
    forward(25)
    circle(i, 4, 5)
    for j in range(20):
        lt(97)
        circle(i * 1.1, j, steps=2)
        circle(i, 2)
update()
done()
        