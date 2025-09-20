from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')

class Score(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.pu()
        self.speed("fastest")
        self.hideturtle()
        self.goto(-10, 275)
        self.count = 0
        self.score_update()

    def collusion(self):
        self.count += 1
        self.clear()
        self.score_update()

    def score_update(self):
        self.write(f'Score: {self.count}', move=False, align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        

