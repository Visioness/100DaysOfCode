from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self):
        super().__init__("square")
        self.color((random.randint(80, 200), random.randint(80, 200), random.randint(80, 200)))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.speed(1)
        self.respawn_car(-320, 320, 5, -500, 500, 5)
        self.move_step = 2


    def move(self):
        self.forward(self.move_step)

    
    def respawn_car(self, y1, y2, ys, x1, x2, xs):
        self.sety(random.randrange(y1, y2, ys))
        self.setx(random.randrange(x1, x2, xs))