# This imports the necessary modules from the Turtle graphics library and the built-in random module.

from turtle import Turtle, Screen
import random

is_race_on = False

# It creates a Screen object and sets up the dimensions of the window to be 500 pixels wide and 400 pixels high.
screen = Screen()
screen.setup(width=500, height=400)
# This line prompts the user to input their bet on the winning turtle's color.
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# Lists are defined for turtle colors and their initial y-positions.
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# This loop creates six turtles, setting their shapes to "turtle", lifting the pen, assigning colors from the colors list, and positioning them at corresponding y-coordinates from y_positions. All turtles are added to the all_turtles list.
all_turtles = []

# Create 6 turtles
for turtle_index in range(0, 6):
	new_turtle = Turtle(shape="turtle")
	new_turtle.penup()
	new_turtle.color(colors[turtle_index])
	new_turtle.goto(x=-230, y=y_positions[turtle_index])
	all_turtles.append(new_turtle)
# Setting Up Race Conditions:
# If the user has provided a bet, the is_race_on flag is set to True.
if user_bet:
	is_race_on = True

# The main loop runs as long as the is_race_on flag is True. For each turtle, it checks if the turtle has crossed the finish line (x-coordinate > 230).
# If a turtle has crossed, it stops the race, determines the winning color, and compares it with the user's bet, providing the result. Turtles move forward a random distance in each iteration.
while is_race_on:
	for turtle in all_turtles:
		# 230 is 250 - half the width of the turtle.
		if turtle.xcor() > 230:
			is_race_on = False
			winning_color = turtle.pencolor()
			if winning_color == user_bet:
				print(f"You've won! The {winning_color} turtle is the winner!")
			else:
				print(f"You've lost! The {winning_color} turtle is the winner!")

		# Make each turtle move a random amount.
		rand_distance = random.randint(0, 10)
		turtle.forward(rand_distance)

screen.exitonclick()
