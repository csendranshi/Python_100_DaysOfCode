from turtle import Turtle, Screen
import random
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

colors = ['blue','cyan','grey','maroon','green','pink','purple','orange','yellow']
directions = [0,90,180,270]
# timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")
for i in range (0,361,5):

    color_tuple = random.choice(colors)
    # color_tuple = (random.randint(0,255)/1000,random.randint(0,255)/1000,random.randint(0,255)/1000)
    timmy_the_turtle.color(color_tuple)
    timmy_the_turtle.circle(100)
    timmy_the_turtle.setheading(i)

screen = Screen()
screen.exitonclick()















screen = Screen()
screen.exitonclick()