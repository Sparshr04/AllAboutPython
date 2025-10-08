from turtle import Turtle, Screen

tom = Turtle()
for _ in range(50):
    tom.pd()
    tom.forward(20)
    tom.pu()
    tom.forward(20)

screen = Screen()
screen.exitonclick()