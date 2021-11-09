from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.x_cord = -200
        self.y_cord = 200
        self.create_score()

    def create_score(self):

        self.penup()
        self.goto(self.x_cord, self.y_cord)
        self.hideturtle()
        self.color("black")
        self.write(arg="Level: "+str(self.score), move=False, align="center", font=FONT)

    def increase(self):
        self.score += 1
        return self.score

    def update_score(self):
        self.clear()
        self.penup()
        self.write(arg="Level: "+str(self.score), move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="G A M E O V E R", move=False, align="center", font=FONT)