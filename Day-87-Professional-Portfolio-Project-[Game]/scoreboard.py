from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, height, remaining_targets):
        super().__init__()
        self.remaining_targets = remaining_targets
        self.height = height
        self.penup()
        self.hideturtle()
        self.color('white')
        self.pensize('5')
        self.speed(0)

    
    def update_score(self):
        self.clear()
        self.goto(0, (self.height / 2) - 80)
        self.write(f'{self.remaining_targets}', align='center', font=('TimesNewRoman', 40, 'bold'))


    def game_over(self, score):
        self.clear()
        self.goto(0, 0)
        self.write(f'Game Over', align='center', font=('TimesNewRoman', 40, 'bold'))
        self.goto(0, -30)
        self.write(f'Score -> {score}', align='center', font=('TimesNewRoman', 25, 'bold'))