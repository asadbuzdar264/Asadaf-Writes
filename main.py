import scoore_board
from snake import Snake
import time
from turtle import Screen
from food import Food
from scoore_board import Scoor_board

#Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Turtle Game")
screen.tracer(0)

#Create Game object
snake = Snake()
food = Food()
score = Scoor_board()

#Control Setup
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")

#Game Loop
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
#Detect collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        score.update_board()
#Detect Collision with Wall
    if snake.head.xcor() > 385 or snake.head.xcor() < -395 or snake.head.ycor() > 385 or snake.head.ycor() < -385:
        is_game_on = False
        score.game_over()

screen.exitonclick()
#Turtle Graphics
#ASADAF Writes