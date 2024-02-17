from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("highest_score.txt", "r") as f:
            self.highest_score = int(f.read())
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update()


    def game_over(self):
        self.goto(0, -50)
        self.write(f"   GAME OVER!\nHighest score is {self.highest_score}!\n\nPress 'f' to restart\nPress 'q' to leave", align="center", font=("Arial", 28, "normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest_score.txt", "w") as f:
                f.write(f"{self.score}")
        self.update()

    
    def update(self):
        self.write(f"Score: {self.score}  -  Highest Score: {self.highest_score}", align="center", font=("Arial", 20, "normal"))