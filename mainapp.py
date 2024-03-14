#this code is broken. the 1st turtle wont move

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)

# Catch the string into a variable
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

# Create the original turtle
tim = Turtle(shape="turtle")
tim.color(colors[0])
tim.penup()
tim.goto(x=-230, y=-100)

# Create and position the additional turtles at the same vertical positions
vertical_gap = 40

for turtle_color in colors[1:6]:  # Exclude the color of the original turtle
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100)

    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)

# Catch the string into a variable
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

# Create the original turtle
tim = Turtle(shape="turtle")
tim.color(colors[0])
tim.penup()
tim.goto(x=-230, y=-100)

# Create and position the additional turtles at the same vertical positions
vertical_gap = 40

for turtle_color in colors[1:6]:  # Exclude the color of the original turtle
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100)

    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()






# I used a loop to create additional turtles for colors [1:6] (excluding the color of the original turtle).
# Each new turtle is created with its shape and color from the loop.
# penup() is used to lift the pen for movement.
# I adjusted the y-coordinate for each new turtle based on the y-coordinate of the original turtle (tim.ycor()) and the specified vertical gap (vertical_gap).
# The turtles.append(new_turtle) line adds each new turtle to the turtles list.
# tim = new_turtle updates the reference to the current turtle for the next iteration.