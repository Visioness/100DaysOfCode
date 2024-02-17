from turtle import Turtle

FONT = ("TimesNewRoman", 40, "bold")
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self, height):
        super().__init__()
        self.height = height
        self.player1 = 0
        self.player2 = 0
        self.penup()
        self.color("white")
        self.pensize(7)
        self.speed(0)


    def midline(self):
        self.hideturtle()
        self.goto(0, (self.height / 2) - 20)
        self.setheading(270)
        while self.ycor() > -(self.height / 2) + 20:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)


    def update_score(self):
        self.clear()
        self.midline()
        self.goto(-100, (self.height / 2) - 80)
        self.write(f"{self.player1}", align=ALIGN, font=FONT)
        self.goto(100, (self.height / 2) - 80)
        self.write(f"{self.player2}", align=ALIGN, font=FONT)
