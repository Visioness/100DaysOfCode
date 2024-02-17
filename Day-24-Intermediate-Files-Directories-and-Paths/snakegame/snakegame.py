from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

HEIGHT = 600
WIDTH = 600

screen = Screen()
screen.setup(height=HEIGHT, width=WIDTH)
screen.title("Snake Game")
screen.tracer(0)

def leave_game():
    screen.bye()

def start_game():
    screen.clear()
    screen.tracer(0)
    score = Scoreboard()
    screen.bgcolor("black")
    snake = Snake()
    food = Food(HEIGHT - 40, WIDTH - 40)
    
    food.spawn_food()
    game_over = False

    screen.listen()
    screen.onkey(snake.turn_left, "a")
    screen.onkey(snake.turn_right, "d")
    screen.onkey(leave_game, "q")
    screen.onkey(start_game, "f")

    while not game_over:
        screen.update()
        time.sleep(0.09)
        snake.move()
        if snake.head.distance(food.food) < 15:
            snake.eat_food()
            score.increase_score()
            food.spawn_food()
                
        if snake.bit_itself() or snake.crash_wall():
            for node in snake.snake:
                node.hideturtle()
            food.food.hideturtle()
            score.game_over()
            screen.mainloop()

start_game()