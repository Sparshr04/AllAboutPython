import turtle as t
import random
assy = t.Turtle()
# colors = ["red", "brown", "green", "yellow", "pink", "violet", "blue"]
t.colormode(255)

angle = [90, 180, 0, 270]
assy.speed("fastest")
assy.width(15)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)

for _ in range(200):
    assy.pencolor(random_color())
    assy.seth(random.choice(angle))
    assy.forward(25)
screen = t.Screen()
screen.exitonclick()
