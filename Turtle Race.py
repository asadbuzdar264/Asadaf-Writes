import turtle, random
from turtle import Turtle, Screen
turtle_color = ["red", "green","blue", "yellow","purple","gray","pink"]
y_cordinates = [190,110,30,-50,-120,-170,-250]
user_choice = turtle.textinput("Turtle Race", "Ready for Race?(y/n)")
#Screen setup
screen =  Screen()
turtle_move = False
screen.setup(width=600,height=500)
totall_turtles = []
#Creating Turtles
for turtles in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(-290, y=y_cordinates[turtles])
    new_turtle.color(turtle_color[turtles])
    totall_turtles.append(new_turtle)
#Race On
if user_choice == "y" or user_choice == "Y":
    turtle_move = True
while turtle_move:
    for item in totall_turtles:
        if item.xcor() > 264:
            turtle_move = False
        # if turtle.xcor() > 270:
        #     is_race_on = False
        distance = random.randint(0,10)
        item.forward(distance)

screen.exitonclick()

#Turtle Graphics
#Asadaf Writes