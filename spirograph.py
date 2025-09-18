import random
import turtle
from turtle import Turtle, Screen
tom = Turtle()
turtle.colormode(255)
# RGB Color
def color():
    r = random.randint(0,155)
    g = random.randint(0,35)
    b = random.randint(0,125)
    color = (r, g, b)
    return color
# For Loop
for i in range(40):
    tom.pencolor(color())
    tom.speed("fastest")
    tom.circle(120)
    tom.left(10)
#Screen Setup
screen = Screen()
screen.exitonclick()

#Turtle Graphics
#Asadaf Writes