from turtle import Turtle, Screen

# tim = Turtle(shape='square')
# tim.color('white')
starting_position = [(0,0), (-20, 0), (-40, 0)]
turtle_body = []

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")

# for turtle in range(0,3):
#     new_part = Turtle(shape='square')
#     new_part.color('white')
#     turtle_body.append(new_part)
for position in starting_position:
    new_segment = Turtle(shape='square')
    new_segment.color('white')
    new_segment.goto(position)
    turtle_body.append(new_segment)

game_is_on = True

while game_is_on:
    for seg in turtle_body:
        seg.forward(20)


# def forward():
#     turtle_body[0].forward(30)
#     position = turtle_body[0].pos()
#     turtle_body[1].goto(-21 + position[0],0 + position[1])
#     turtle_body[2].goto(-41 + position[0],0 + position[1])
    

# def left():
#     turtle_body[0].left(90)
#     position = turtle_body[0].pos()
#     turtle_body[1].goto(-21 + position[0],0 + position[1])
#     turtle_body[2].goto(-41 + position[0],0 + position[1])

# def right():
#     turtle_body[0].right(90)
#     position = turtle_body[0].pos()
#     turtle_body[1].goto(-21 + position[0],0 + position[1])
#     turtle_body[2].goto(-41 + position[0],0 + position[1])

# ________________Initial Trial code set__________________________
# position = turtle_body[0].pos()
# turtle_body[1].goto(-21 + position[0],0 + position[1])
# turtle_body[2].goto(-41 + position[0],0 + position[1])
# turtle_body[3].goto(-21,0)
# _________________________________________________________________


# screen.listen()
# screen.onkey(key='w', fun=forward)
# screen.onkey(key='a', fun=left)
# screen.onkey(key='d', fun=right)
screen.exitonclick()