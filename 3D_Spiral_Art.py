import turtle
import colorsys
import time
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(0)
h=0 
s.tracer(1,0)

for i in range(200):
    c=colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(c)
    h+=0.005
    t.forward(i*2)
    t.right(121)
    t.width(2)
    
turtle.done() 