from turtle import Turtle
FONT = ("Arial", 15, "normal")
LV_POS =(-260, 270)
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(LV_POS)
        self.write(f"Level: {self.level}", align="center", font= FONT)

#Asadaf Writes