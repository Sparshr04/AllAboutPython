from turtle import Turtle, Screen
from random import choice
ass = Turtle()
colors = ["red", "brown", "green", "yellow", "pink", "violet", "blue"]

for angle in range(3,10):
    ass.color(choice(colors))
    # ass.right(360/angle)
    for steps in range(angle):

       ass.forward(100)
       ass.right(360/angle)
    

screen = Screen()
screen.exitonclick()