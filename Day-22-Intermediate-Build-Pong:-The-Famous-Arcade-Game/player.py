from turtle import Turtle, Screen

PADDLE_LENGTH = 3
PADDLE_SHAPE = "square"

class Player():
    def __init__(self, x, y):
        self.create_paddle(x, y)


    def create_paddle(self, x, y):
        self.paddle = Turtle(PADDLE_SHAPE)
        self.paddle.penup()
        self.paddle.setheading(90)
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.color("white")
        self.paddle.goto(x, y)
        

    def paddle_up(self):
        self.paddle.setheading(90)
        if self.paddle.ycor() < 360:
            self.paddle.forward(20)


    def paddle_down(self):
        self.paddle.setheading(270)
        if self.paddle.ycor() > -360:
            self.paddle.forward(20)