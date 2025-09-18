import random, turtle
from turtle import Turtle, Screen
#Screen Setup:
screen = Screen()
screen.setup(width=700, height=550)
#Turtle Setup:
timmy = Turtle("turtle")
timmy.penup()
timmy.goto(-215, -110)
timmy.speed(2)
timmy.shapesize(1.5)
#Color Setup:
turtle.colormode(255)
color_list = colors = [(150, 20, 60), (253, 47, 156), (123, 104, 238), (255, 108, 71), (46, 139, 87), (255, 2, 137),
                       (72, 61, 139), (65, 234, 41), (199, 21, 133), (100, 149, 25),(47, 160, 122), (42, 39, 116),
                       (255, 99, 102), (106, 90, 168),(0, 94, 127), (255, 215, 0), (65, 105, 225), (255, 69, 0), (1, 217, 255), (186, 85, 211),
                       (74, 21, 181), (60, 179, 113), (255, 20, 147), (32, 178, 170), (244, 164, 96), (147, 112, 219),
                       (210, 105, 30), (135, 206, 235), (219, 112, 147),(127, 255, 0), (139, 69, 19), (176, 224, 230), (218, 165, 32), (0, 128, 128),
                       (255, 250, 205), (70, 130, 180), (255, 240, 245), (25, 25, 112), (240, 230, 140), (0, 100, 0)]
#Final Code:
def movment():
    for i in range(15):
        color = random.choice(color_list)
        timmy.dot(20, color)
        timmy.penup()
        timmy.color(color)
        timmy.forward(30)
        timmy.pendown()
def move_left():
    timmy.left(90)
    color = random.choice(color_list)
    timmy.dot(20, color)
    timmy.penup()
    timmy.forward(30)
    timmy.pendown()
    timmy.left(90)
def move_right():
    timmy.right(90)
    timmy.dot(20,"red")
    timmy.penup()
    timmy.forward(30)
    timmy.pendown()
    timmy.right(90)
def final_movment():
    for i in range(4):
        movment()
        move_left()
        movment()
        move_right()

final_movment()
screen.exitonclick()

#Turtle Graphics
#Asadaf Writes
