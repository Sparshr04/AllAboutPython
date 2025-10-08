import colorgram

colors = colorgram.extract("hirst_spot.jpg", 30)
list_colors = []

# __________This method was good but the output was not quiet neede______
# OUTPUT: ['(r=252, g=251, b=248)', '(r=219, g=173, b=124)', '(r=159, g=180, b=190)', '(r=134, g=73, b=53)', '(r=49, g=102, b=153)', '(r=245, g=232, b=236)']
# print(colors[0])
# for color in colors:
#     list_colors.append(color.rgb)

# color_list = [str(obj) for obj in list_colors]
# ass = [color.removeprefix('Rgb') for color in color_list]
# print(ass)

#What we need

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     list_colors.append(new_color)

# print(list_colors)

# OUTPUT = [(219, 173, 124), (159, 180, 190), (134, 73, 53), (49, 102, 153), (245, 232, 236), (118, 82, 93), (179, 140, 150), (247, 251, 248), (41, 46, 65), (162, 104, 151), (126, 173, 114), (83, 96, 183), (67, 9, 27), (238, 241, 245), (81, 133, 107), (231, 188, 138), (52, 62, 79), (195, 90, 72), (116, 43, 58), (60, 41, 28), (92, 144, 117), (70, 67, 52), (182, 187, 207), (211, 181, 189), (102, 51, 38), (174, 199, 203), (181, 201, 180), (210, 184, 180), (41, 73, 82)]

import turtle
import random
ass = turtle.Turtle()
turtle.colormode(255)

rgb_list = [(219, 173, 124), (159, 180, 190), (134, 73, 53), (49, 102, 153), (245, 232, 236), (118, 82, 93), (179, 140, 150), (247, 251, 248), (41, 46, 65), (162, 104, 151), (126, 173, 114), (83, 96, 183), (67, 9, 27), (238, 241, 245), (81, 133, 107), (231, 188, 138), (52, 62, 79), (195, 90, 72), (116, 43, 58), (60, 41, 28), (92, 144, 117), (70, 67, 52), (182, 187, 207), (211, 181, 189), (102, 51, 38), (174, 199, 203), (181, 201, 180), (210, 184, 180), (41, 73, 82)]

x = -200
y = -150

ass.speed('fastest')
ass.pu()
ass.goto(x,y)

for multiple in range(1,11):
    for _ in range(10):
        ass.dot(20)
        ass.pencolor(random.choice(rgb_list))
        ass.forward(50)

    ass.goto(x,y+50*(multiple))
# print(turtle.screensize())

screen = turtle.Screen()
screen.exitonclick()
