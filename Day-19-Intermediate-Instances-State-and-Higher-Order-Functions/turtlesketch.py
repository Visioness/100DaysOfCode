from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(30)


def move_backward():
    turtle.backward(30)


def turn_left():
    turtle.setheading(turtle.heading() + 10)


def turn_right():
    turtle.setheading(turtle.heading() - 10)


def clear():
    turtle.penup()
    turtle.clear()
    turtle.home()
    turtle.pendown()

turtle.speed(1)
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_right, "Right")
screen.onkey(turn_left, "Left")
screen.onkey(clear, "c")
screen.exitonclick()
