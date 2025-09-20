from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Check collison with food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        score.collusion()
        snake.extend()

    #detect collusion with food
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    #detect collusion with tail
    # We can either loop through the segments in the snake body. Except the head.
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 18:
    #         game_is_on = False
    #         score.game_over()


    #Or we can use String Slicing in Python. Here instead of writing a IF_ELIF statement, we can just slice the 
    #string saving use some Time complexity and moving us to professionalism
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 18:
            game_is_on=False
            score.game_over()


screen.exitonclick()