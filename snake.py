from turtle import Turtle
# Constants Setup
STARTING_POSITION = [(0,0),(20,0),(40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
#Snake Class Setup
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
# Create the Initial Snake
    def create_snake(self):
        for position in STARTING_POSITION:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.segments.append(snake)
# Move the Snake Forward
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_axis = self.segments[seg_num - 1].xcor()
            y_axis = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_axis, y_axis)
        self.head.forward(20)
#Control Setup
    def up(self):
        if self.head.heading() != DOWN:  # snake not moving down
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:  # snake not moving up
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:  # snake not moving right
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:  # snake not moving left
            self.head.setheading(RIGHT)

#Turtle Graphics
#ASADAF Writes