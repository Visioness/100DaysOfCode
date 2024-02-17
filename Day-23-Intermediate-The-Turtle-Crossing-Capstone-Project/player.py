from turtle import Turtle

MOVE_STEP = 4

class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.color("black")
        self.speed(1)
        self.penup()
        self.setheading(90)
        self.goto(0, -400)
    
    def move(self):
        self.forward(MOVE_STEP)