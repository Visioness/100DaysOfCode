from turtle import Turtle
import random

class Target(Turtle):
    def __init__(self, width, height, color):
        super().__init__()
        self.shape('square')
        self.speed(1)
        self.penup()
        self.color(color)
        self.pencolor('grey')
        self.shapesize(stretch_len=4, stretch_wid=1.5, outline=3)
        self.hideturtle()
        self.spawn_target(width, height)


    def spawn_target(self, width, height):
        self.goto(width, height)
        self.showturtle()