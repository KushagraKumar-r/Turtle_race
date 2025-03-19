from turtle import Turtle, Screen

# Create a turtle and screen
screen = Screen()
screen.setup(width=500, height=400)

# Ask user to make the bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors=["red","orange","yellow","green","blue","purple"]
y_position=[-70,-40,-10,20,50,80]


for turtle_index in range(0,6):
    tim = Turtle()
    tim.color(colors[turtle_index])
    tim.shape("turtle")
    tim.penup()
    # this step will place the turtle at any of position in screen ,but right now we are placing it at extreme left of stream tim.goto(-240,0)
    tim.goto(-240,y_position[turtle_index])



# Wait for a click to exit
screen.exitonclick()


