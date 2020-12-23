from turtle import Turtle, Screen
import random
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

colors = ['blue','cyan','grey','maroon','green','pink','purple','aqua','violet']
directions = [0,90,180,270]
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")
for i in range (0,500):

    color_tuple = (random.randint(0,255)/1000,random.randint(0,255)/1000,random.randint(0,255)/1000)
    timmy_the_turtle.color(color_tuple)
    timmy_the_turtle.forward(20)
    timmy_the_turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()















screen = Screen()
screen.exitonclick()