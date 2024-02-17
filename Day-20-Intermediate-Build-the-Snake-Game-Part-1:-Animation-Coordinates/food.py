from turtle import Turtle, Screen
import random

class Food():
    def __init__(self, height=560, width=560):
        self.height = height
        self.width = width
        self.food = Turtle("turtle")
        self.food.shapesize(0.6, 0.6)
        self.food.penup()
        self.food.color("orange")
        
    
    def spawn_food(self):         
        self.food.goto(self.randomize(self.height), self.randomize(self.width))


    def randomize(self, length):
        return random.randrange(-(length / 2), (length / 2), 20)