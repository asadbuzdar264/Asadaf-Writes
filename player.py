from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.shapesize(1.2)
        self.setheading(90)
    def position(self):
        self.goto(x=0, y= -280)
    def up(self):
        self.forward(13)
    def movement(self):
        if self.ycor() > 290:
            self.goto(x=0, y=-280)

#Asadaf Writes