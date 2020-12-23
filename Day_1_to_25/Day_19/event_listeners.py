from turtle import *

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_back():
    tim.backward(10)

def turn_right():
    tim.right(90)

def turn_left():
    tim.left(90)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c',fun=clear)
screen.exitonclick()