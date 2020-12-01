from turtle import *
import random

is_race = False
screen = Screen()
screen.setup(width=500,height=400)

user_bet =screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ['red','orange','yellow','green','blue','purple']
all_turtles = []

for i in range(len(colors)):

    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=-70 + (30*i))
    all_turtles.append(new_turtle)


if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
            break
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
screen.exitonclick()