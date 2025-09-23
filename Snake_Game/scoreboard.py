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
        # self.high_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score_update()

    def collusion(self):
        self.count += 1
        self.clear()
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f'Score: {self.count} | High Score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.count > self.high_score:
            self.high_score = self.count
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.count = 0
        self.score_update()
        

