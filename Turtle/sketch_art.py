import turtle

ass = turtle.Turtle()

#Move Forward
def move_forward():
    ass.forward(10)

#Turn Left
def turn_left():
    new_heading = ass.heading() + 10
    ass.seth(new_heading)

#Turn Right
def turn_right():
    new_heading = ass.heading() - 10
    ass.seth(new_heading)

#Move Backwards
def move_back():
    ass.back(10)

#clear screen
def clear():
    ass.clear()


screen = turtle.Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="c", fun=clear)
screen.exitonclick()

