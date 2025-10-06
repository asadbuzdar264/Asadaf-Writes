import time
from turtle import Screen
from player import Player
from cars import CarManager
from scoreboard import ScoreBoard
#Setting up Screen
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
#Object Creation
timm = Player()
timm.position()
carmanager = CarManager()
scooreboard = ScoreBoard()
screen.listen()
screen.onkey(timm.up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    carmanager.create_car()
    carmanager.move_cars()
    screen.update()
    for car in carmanager.all_car:
        if car.distance(timm) < 25:
            timm.goto(0,0)
            timm.write("Game Over", False, "center", ("Arial", 16, "bold"))
            game_on = False
        timm.movement()
screen.exitonclick()

#Turtle Crossing Game
#Asadaf Writes