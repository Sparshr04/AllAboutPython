import turtle as t
import random


screen = t.Screen()

# ass = t.Turtle()
# bss = t.Turtle()
# wss = t.Turtle()
# qww = t.Turtle()
# sdd = t.Turtle()

# ass.color('red')
# bss.color('green')
# wss.color('purple')
# qww.color('black')
# sdd.color('yellow')

# for turtle in screen.turtles():
#     turtle.shape('turtle')
#     turtle.pu()


screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!",  prompt="Which turtle will win the race? Enter a color: ")

# ass.goto(-230, -170)
# bss.goto(-230, -90)
# wss.goto(-230, -10)
# qww.goto(-230, 70)
# sdd.goto(-230, 130)

# def move_forward():

#     ass.forward(random.randint(1,20))
#     bss.forward(random.randint(1,20))
#     wss.forward(random.randint(1,20))
#     qww.forward(random.randint(1,20))
#     sdd.forward(random.randint(1,20))

# is_race_over = False

# for _ in range(60):
#     move_forward()
#     for turtle in screen.turtles():
#         if turtle.xcor() >= 230:
#             color = turtle.pencolor()
#             if user_bet == color:
#                 print('You Got that right!')
#                 # break 
#             else:
#                 print(f'You Lost, {color} turtle won.')
#                 # break
#             is_race_over = True
#             break
#     if is_race_over:
#         break

# Way better Method than writing it individually like above
y_chordinate = [-170, -90, -10, 70, 130 ]
colors = ['red', 'green', 'yellow', 'purple', 'blue']
all_turtles = []
for turtle_index in range(0,5):
        new_turtle = t.Turtle(shape='turtle')
        new_turtle.pu()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(-230, y_chordinate[turtle_index])
        all_turtles.append(new_turtle)


if user_bet:
        is_race_on = True

while is_race_on:
        
        for turtle in all_turtles:
                if turtle.xcor() > 230:
                        is_race_on = False
                        winning_color = turtle.pencolor()
                        if winning_color == user_bet:
                                print('You Got that right!')
                        else:
                               print(f'You Lost, {winning_color} turtle won.')

                 

                rand_distance = random.randint(1,20)
                turtle.forward(rand_distance)






        
screen.exitonclick()
