from turtle import Turtle
from turtle import Screen
from targets import Target
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import random
import time

WIDTH = int(1920 * 0.85)
HEIGHT = int(1080 * 0.9)
COLORS = ['blue', 'purple', 'red', 'orange', 'yellow']

screen = Screen()
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)
screen.setup(width=WIDTH, height=HEIGHT, starty=20)


# Spawning each target as a turtle
spawn_y = (HEIGHT / 3 - 100)
targets = []
for i in range(5):
    spawn_x = (-WIDTH / 2 + 45)
    while spawn_x < (WIDTH / 2):
        target = Target(width=spawn_x, height=spawn_y, color=COLORS[i])
        targets.append(target)
        spawn_x += 90
    spawn_y += 40

target_count = len(targets)


# Creating instances for ball, paddle and scoreboard
ball = Ball()
paddle = Paddle()
scoreboard = Scoreboard(remaining_targets=target_count, height=HEIGHT)

# Listening key presses to move paddle
screen.listen()
screen.onkey(paddle.move_left, 'Left')
screen.onkey(paddle.move_left, 'a')
screen.onkey(paddle.move_right, 'Right')
screen.onkey(paddle.move_right, 'd')

is_game_over = False
while not is_game_over:
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    paddle_x = paddle.xcor()
    paddle_y = paddle.ycor()

    # Game over
    if ball_y < (-HEIGHT / 2) + 20:
        is_game_over = True
        scoreboard.game_over(target_count - scoreboard.remaining_targets)
        break

    # Window top collision
    if ball_y > (HEIGHT / 2) - 20:
        ball.setheading(180 + (90 - (ball.heading() - 90)))
    
    # Window walls collisions
    if abs(ball_x) > WIDTH / 2 - 20:
        ball.setheading(180 + (180 - (ball.heading() - 180)))

    # Target collision conditions
    for target in targets:
        target_x = target.xcor()
        target_y = target.ycor()
        if ball.distance(target) < 55:
            # Creating different distance rules for each side of the target
            if 180 < ball.heading() < 360 and target_x - 40 < ball_x < target_x + 40 and ball.distance(ball_x, target_y + 15) < 12:
                target.hideturtle()
                targets.remove(target)
                ball.setheading(360 - ball.heading())
                scoreboard.remaining_targets -= 1
                
            elif 0 < ball.heading() < 180 and target_x - 40 < ball_x < target_x + 40 and ball.distance(ball_x, target_y - 15) < 12:
                target.hideturtle()
                targets.remove(target)
                ball.setheading(360 - ball.heading())
                scoreboard.remaining_targets -= 1

            elif -90 < ball.heading() < 90 and target_y - 15 < ball_y < target_y + 15 and ball.distance(target_x + 40, ball_y) < 12:
                target.hideturtle()
                targets.remove(target)
                ball.setheading(180 - ball.heading())
                scoreboard.remaining_targets -= 1

            elif 90 < ball.heading() < 270 and target_y - 15 < ball_y < target_y + 15 and ball.distance(target_x - 40, ball_y) < 12:
                target.hideturtle()
                targets.remove(target)
                ball.setheading(180 - ball.heading())
                scoreboard.remaining_targets -= 1

    # Paddle Collision   
    if 180 < ball.heading() < 360 and paddle_x - 90 < ball_x < paddle_x + 90 and ball.distance(ball_x, paddle_y + 10) < 12:
        ball.setheading(180 + (90 - (ball.heading() - 90)) + random.randint(-15, 15))

    screen.update()
    scoreboard.update_score()
    time.sleep(0.001)
    ball.move()

screen.mainloop()