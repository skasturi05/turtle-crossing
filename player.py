STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.finish_line_y = FINISH_LINE_Y

    def up(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        if self.ycor() >= self.finish_line_y:
            self.goto(STARTING_POSITION)
