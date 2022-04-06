from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.color('green')


def side(n=1):
    for i in range(n):
        timmy.forward(100)
        timmy.right(90)


def dashed_line(n=1):
    for i in range(n):
        timmy.forward(5)
        timmy.penup()
        timmy.forward(5)
        timmy.pendown()


def shapes(n=3):
    for i in range(n+1):
        if i >= 3:
            degrees = 360/i
            for _ in range(i):
                timmy.forward(100)
                timmy.right(degrees)


def random_walk():
    timmy.shape('arrow')
    timmy.speed(10)
    timmy.width(10)
    for _ in range(300):
        colormode(255)
        timmy.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        timmy.right(360/random.randint(1, 4))
        timmy.forward(25)


def spirograph(size_of_gap):
    timmy.shape('arrow')
    timmy.speed(0)
    for _ in range(size_of_gap):
        timmy.setheading(timmy.heading()+10)
        colormode(255)
        timmy.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        timmy.circle(100)


random_walk()
screen = Screen()
screen.exitonclick()
