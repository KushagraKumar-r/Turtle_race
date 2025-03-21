# from turtle import Turtle, Screen
# import random

# is_race_on=False
# # Create a turtle and screen
# screen = Screen()
# screen.setup(width=500, height=400)

# # Ask user to make the bet
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# colors=["red","orange","yellow","green","blue","purple"]
# y_positions=[-70,-40,-10,20,50,80]
# all_turtles=[]


# for turtle_index in range(0,6):
#     new_turtle = Turtle()
#     new_turtle.color(colors[turtle_index])
#     new_turtle.shape("turtle")
#     new_turtle.penup()
#     # this step will place the turtle at any of position in screen ,but right now we are placing it at extreme left of stream tim.goto(-240,0)
#     new_turtle.goto(x=-240, y=y_positions[turtle_index])
#     all_turtles.append(new_turtle)


# if user_bet:
#     is_race_on=True

# while is_race_on:

#     for turtle in all_turtles:
#         if turtle.xcor()>240:
#             print(turtle.color())

#         random_distance=random.randint(0,10)
#         turtle.forward(random_distance)


# # Wait for a click to exit
# screen.exitonclick()

from turtle import Turtle, Screen
import random

is_race_on = False
# Create a turtle and screen
screen = Screen()
screen.setup(width=500, height=400)

# Ask user to make the bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    # new_turtle.shape("turtle")
    new_turtle.goto(x=-230, y=y_positions[turtle_index]) 
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        # Check if the turtle has crossed the finish line
        if turtle.xcor() > 240:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break  # Exit the for loop if a turtle has won

# Wait for a click to exit
screen.exitonclick()