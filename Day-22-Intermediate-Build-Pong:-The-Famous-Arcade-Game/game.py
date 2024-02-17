from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from ball import Ball
import time

HEIGHT = 800
WIDTH = 1400

screen = Screen()
screen.setup(height=HEIGHT, width=WIDTH)
screen.bgcolor("black")
screen.tracer(0)

player1 = Player(-650, 0)
player2 = Player(650, 0)
scoreboard = Scoreboard(HEIGHT)
ball = Ball()

screen.listen()
screen.onkey(player1.paddle_down, "s")
screen.onkey(player1.paddle_up, "w")
screen.onkey(player2.paddle_down, "Down")
screen.onkey(player2.paddle_up, "Up")

game_over = False
while not game_over:
    if abs(ball.ycor()) > 380:
        ball.setheading(180 + (90 - (ball.heading() - 90)))

    if (-620 > ball.xcor() > player1.paddle.xcor() and ball.distance(player1.paddle) < 50) or (620 < ball.xcor() < player2.paddle.xcor() and ball.distance(player2.paddle) < 50):
        ball.setheading(180 + (180 - (ball.heading() - 180)))

    if ball.xcor() < -700:
        scoreboard.player2 += 1
        ball.spawn_ball()

    elif ball.xcor() > 700:
        scoreboard.player1 += 1
        ball.spawn_ball()
    
    scoreboard.update_score()
    screen.update()
    time.sleep(0.00005)
    ball.move()


screen.exitonclick()