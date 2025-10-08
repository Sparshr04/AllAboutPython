import turtle as t
import random

t.colormode(255)
ass = t.Turtle()
ass.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)
# __________________________________
#METHOD 1 (by me)

# for num in range(1,360):
#     ass.pencolor(random_color())
#     ass.circle(100)
#     ass.seth(num)

# ______________________________________


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        ass.pencolor(random_color())
        ass.circle(100)
        ass.seth(ass.heading()+size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()