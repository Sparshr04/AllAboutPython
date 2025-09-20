from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.construct()
        self.head = self.segments[0]
        
    def construct(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.pu()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def join_logic(self):
        for segment in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment-1].xcor()
            new_y = self.segments[segment-1].ycor()
            self.segments[segment].goto(new_x, new_y)

    def move(self):
        self.join_logic()
        self.head.forward(MOVE_DIST)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(90)
        

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(0)