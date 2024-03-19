from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.pencolor('grey')
        self.speed(0)
        self.penup()
        self.spawnball(0, 0)
        

    def spawnball(self, width, height):
        self.goto(width, height)
        self.setheading(random.randint(30, 150))
    

    def move(self):
        self.forward(3)