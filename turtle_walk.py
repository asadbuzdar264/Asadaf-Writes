import random
import turtle
from turtle import Turtle, Screen
gibby = Turtle()
gibby.speed("fastest")
direction = [0,90,180,270]
turtle.colormode(255)
# For RGB Color
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color
# For loop
for i in range(200):
    gibby.pensize(5)
    gibby.pencolor(random_color())
    gibby.forward(15)
    gibby.right(random.choice(direction))
#Screen Setup
screen = Screen()
screen.exitonclick()

#Turtle Graphics
#Asadaf Writes