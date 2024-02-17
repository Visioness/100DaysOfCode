from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=600, width=1000)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for color in colors:
    turtle = Turtle()
    turtle.speed(1)
    turtle.shape("turtle")
    turtle.color(color)
    turtle.penup()

y = -90
for turtle in screen.turtles():
    turtle.setposition(-450, y)
    y += 40

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle wins? Enter the color: ").lower()

won = False
while not won:
    for turtle in screen.turtles():
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() > 300:
            won = True
            color_won = turtle.pencolor()
            if user_bet == color_won:
                turtle.write(f"You won! {color_won.capitalize()} turtle has won the race!", move=False, align="left", font=('TimesNewRoman', 10, 'bold'))
                # print(f"You won! {color_won.capitalize()} turtle has won the race!")
            else:
                turtle.write(f"You lost! {color_won.capitalize()} turtle has won the race!", move=False, align="left", font=('TimesNewRoman', 10, 'bold'))
                # print(f"You lost! {color_won.capitalize()} turtle has won the race!")
            break

screen.exitonclick()