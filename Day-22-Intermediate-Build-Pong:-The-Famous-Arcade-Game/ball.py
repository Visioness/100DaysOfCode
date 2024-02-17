from turtle import Turtle
import random
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.speed(0)
        self.showturtle()
        self.spawn_ball()


    def move(self):
        self.forward(2)

    
    def spawn_ball(self):
        self.goto(0, 0)
        self.setheading(-90 -(90 - self.heading()) + random.randrange(-45, 45))
        
