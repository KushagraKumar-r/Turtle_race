# from turtle import Turtle,Screen
# tim=Turtle()
# tim.shape("turtle")
# screen=Screen()

# def move_forwards():
#     tim.forward(10)

# screen.listen()
# screen.onkey(key="space",fun=move_forwards)
# screen.exitonclick()
from turtle import Turtle,Screen

tim=Turtle()
tim.shape("turtle")
tim.color("aqua")
screen=Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key="space",fun=move_forwards)
screen.exitonclick()