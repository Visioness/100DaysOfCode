from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.goto(-360, 340)
        self.level = 1
        self.update_board()

    
    def update_board(self):
        self.clear()
        self.write(f"Level: {self.level}", font=("Arial", 28, "normal"))
