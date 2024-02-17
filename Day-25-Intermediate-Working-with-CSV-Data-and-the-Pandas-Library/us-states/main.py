from turtle import Turtle, Screen
import pandas

screen = Screen()

screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
lives = 5

while lives > 0:
    guess = screen.textinput("Guess State", "Guess a US State!").title()
    if guess in states:
        guess_data = data[data.state == guess]
        turtle = Turtle("turtle")
        turtle.penup()
        turtle.speed(1)
        turtle.goto(int(guess_data.x.iloc[0]), int(guess_data.y.iloc[0]))
        turtle.hideturtle()
        turtle.write(guess, move=True)
        
        

    else:
        lives -= 1

screen.exitonclick()