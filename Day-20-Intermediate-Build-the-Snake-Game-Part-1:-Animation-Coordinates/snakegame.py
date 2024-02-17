from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

HEIGHT = 600
WIDTH = 600

screen = Screen()

screen.setup(height=HEIGHT, width=WIDTH)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food(HEIGHT - 40, WIDTH - 40)
score = Scoreboard()

food.spawn_food()

while not snake.bit_itself() and  not snake.crash_wall():
    if snake.head.distance(food.food) < 15:
        snake.eat_food()
        score.increase_score()
        food.spawn_food()
    screen.update()
    time.sleep(0.08)

    screen.listen()
    screen.onkey(snake.turn_left, "a")
    screen.onkey(snake.turn_right, "d")
    snake.move()

for turtle in screen.turtles():
    turtle.hideturtle()
score.game_over()
screen.update()

        
    
screen.exitonclick()