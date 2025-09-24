import random
from turtle import Turtle
# Food Setup
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.refresh()  # Place food at a random position
    # Move food to a new random location
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

# Turtle Graphics
# ASADAF Writes
