import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list =[(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35)]
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.shape("circle")
tim.pendown()
number_of_dots = 100
tim.speed("fastest")
tim.hideturtle()

for i in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.penup()
    tim.forward(50)
    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()