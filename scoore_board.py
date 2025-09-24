from turtle import Turtle
#Scoore Board Setup
class Scoor_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-20, 370)
        self.speed("fastest")
        self.hideturtle()
        self.update_Scoreboard()
        # Scoore Board Setup
    def update_Scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "bold"))
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 16, "bold"))

    def update_board(self):
        self.score += 1
        self.update_Scoreboard()

#Turtle Graphics
#ASADAF Writes