from turtle import Turtle, Screen
import random
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

colors = ['blue','red','green','yellow','pink','purple','aqua','violet']
for i in range (4,11):
    angle = 360/ i
    timmy_the_turtle.color(random.choice(colors))
    for j in range(0,i):
        timmy_the_turtle.forward(70)
        timmy_the_turtle.right(angle)

screen = Screen()
screen.exitonclick()















screen = Screen()
screen.exitonclick()