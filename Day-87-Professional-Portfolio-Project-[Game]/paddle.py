from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=9, stretch_wid=1, outline=5)
        self.penup()
        self.color('white')
        self.pencolor('grey')
        self.speed(0)
        self.hideturtle()
        self.spawn_paddle()


    def spawn_paddle(self):
        self.goto(x=0, y=(-(1080 * 0.9 / 2) + 20))
        self.showturtle()


    def move_right(self):
        self.forward(30)
    

    def move_left(self):
        self.back(30)