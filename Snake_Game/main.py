from turtle import Turtle, Screen

# tim = Turtle(shape='square')
# tim.color('white')
turtle_body = []
for turtle in range(0,3):
    new_part = Turtle(shape='square')
    new_part.color('white')
    turtle_body.append(new_part)


def forward():
    turtle_body[0].forward(30)
    position = turtle_body[0].pos()
    turtle_body[1].goto(-21 + position[0],0 + position[1])
    turtle_body[2].goto(-41 + position[0],0 + position[1])
    

def left():
    turtle_body[0].left(90)
    position = turtle_body[0].pos()
    turtle_body[1].goto(-21 + position[0],0 + position[1])
    turtle_body[2].goto(-41 + position[0],0 + position[1])

def right():
    turtle_body[0].right(90)
    position = turtle_body[0].pos()
    turtle_body[1].goto(-21 + position[0],0 + position[1])
    turtle_body[2].goto(-41 + position[0],0 + position[1])

# position = turtle_body[0].pos()
# turtle_body[1].goto(-21 + position[0],0 + position[1])
# turtle_body[2].goto(-41 + position[0],0 + position[1])
# turtle_body[3].goto(-21,0)


screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='a', fun=left)
screen.onkey(key='d', fun=right)
screen.exitonclick()