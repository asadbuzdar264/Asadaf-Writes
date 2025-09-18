import random
from turtle import Turtle, Screen
timmy = Turtle()
color = ["red","green","blue", "pink","yellow", "orange","brown","gray","black","purple"]
def draw_shape(num_side):
    angel = 360 / num_side
    for i in range(num_side):
        timmy.forward(100)
        timmy.right(angel)
for num_of_side in range(3,11):
    draw_shape(num_of_side)
    timmy.color(random.choice(color))
screen = Screen()
screen.exitonclick()

#Turtle Graphics
#Asadaf Writes
