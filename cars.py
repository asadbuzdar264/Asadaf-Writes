import random
from turtle import Turtle
COLOUR= ["red","green","blue","orange","purple","pink"]
y_axis = (-240,-210,-180,-150,-120,-90,-60,-30,0,30,60,90,120,150,180,210,240)
class CarManager:
    def __init__(self):
        self.all_car = []
    def create_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:  # only sometimes create a car
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(random.choice(COLOUR))
            new_car.shapesize(stretch_wid=0.7,stretch_len=1.1)
            new_car.goto(x=300, y=random.choice(y_axis))
            self.all_car.append(new_car)
    def move_cars(self):
        """Move all cars left across the screen"""
        for car in self.all_car:
            car.setx(car.xcor() - 10)  # move left by 20 pixels
    def remove_offscreen_cars(self):
        """Remove cars that have gone off the left side of the screen"""
        for car in self.all_car:
            if car.xcor() < -320:
                car.hideturtle()
                self.all_car.remove(car)

#Asadaf Writes