from turtle import Screen
from player import Player
from cars import Car
from scoreboard import Scoreboard
import time
import random


HEIGHT = 800
WIDTH = 1000
NUMBER_OF_CARS = 30
SLEEP_TIMES = [0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6 , 1.8, 2]
SPEED_MULTIPLIER = 1.2

screen = Screen()
screen.colormode(255)
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)

scoreboard = Scoreboard()

turtle = Player()

cars = [Car() for car in range(NUMBER_OF_CARS)]

screen.listen()
screen.onkey(turtle.move, "w")

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.01)
    for car in cars:
        if car.xcor() < -500:
            car.respawn_car(-320, 320, 5, 500, 550, 5)
        car.move()
        if abs(car.ycor() - turtle.ycor()) < 22 and abs(car.xcor() - turtle.xcor()) < 24:
            game_over = True
            break

    if turtle.ycor() > 370:
        turtle.goto(0, -400)
        scoreboard.level += 1
        scoreboard.update_board()
        for car in cars:
            car.respawn_car(-320, 320, 5, -500, 500, 5)
            car.move_step = scoreboard.level * SPEED_MULTIPLIER
        time.sleep(1)
    

turtle.hideturtle()
turtle.goto(0, 0)
screen.clear()
turtle.write(f"GAME OVER! Final score is -> {scoreboard.level}", align="center", font=("Arial", 32, "normal"))
screen.update()
    
screen.exitonclick()