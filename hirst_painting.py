import turtle

import colorgram as cg
from turtle import Turtle, Screen, colormode
import random

# def painting(image, color_palette=10):
#     colors = cg.extract(image, color_palette)
#     color_list = []
#     for i in range(color_palette):
#         color_list.append(colors[i].rgb[:])
#     return color_list
#
#
# painting('hirst.jpg', 30)

# colors = cg.extract('hirst.jpg', 30)
# color_list = []
# for i in range(len(colors)):
#     color_list.append(colors[i].rgb[:])

timmy = Turtle()
timmy.shape('turtle')
color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216),
              (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177),
              (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28),
              (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8),
              (233, 66, 34)]

counter = 0
#timmy.hideturtle()
timmy.penup()
timmy.setposition(x=-250, y=250)
timmy.pendown()
colormode(255)
timmy.speed('fastest')
draw = True
while draw:
    counter += 1
    timmy.dot(20, random.choice(color_list))
    timmy.penup()
    if counter % 10 == 0:
        timmy.right(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.backward(50*9)
    else:
        timmy.forward(50)
    timmy.pendown()
    if counter == 100:
        draw = False

screen = Screen()
screen.exitonclick()
