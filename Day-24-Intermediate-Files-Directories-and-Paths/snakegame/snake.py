from turtle import Turtle

SNAKE_SIZE = 4
SNAKE_SHAPE = "square"
MOVE_DISTANCE = 20

class Snake():

    def __init__(self):
        self.snake = [Turtle(SNAKE_SHAPE) for i in range(SNAKE_SIZE)]
        xcor = 0
        for node in self.snake:
            node.speed(1)
            node.penup()
            node.color("white")
            node.setx(xcor)
            xcor += 20
        self.snake.reverse()
        self.head = self.snake[0]
        

    def move(self):
        for node_num in range(len(self.snake) - 1, 0, -1):
            self.snake[node_num].setpos(self.snake[node_num - 1].pos())
            self.snake[node_num].setheading(self.snake[node_num - 1].heading())
        self.head.forward(MOVE_DISTANCE)

    
    def crash_wall(self):
        if self.head.xcor() <= -300 or self.head.xcor() >= 300 or self.head.ycor() <= -300 or self.head.ycor() >= 300:
            return True

    
    def eat_food(self):
        turtle = Turtle(SNAKE_SHAPE)
        turtle.color("white")
        position = self.snake[-1].pos()
        turtle.penup()
        turtle.setposition(position)
        self.snake.append(turtle)


    def turn_left(self):
        self.head.left(90)


    def turn_right(self):
        self.head.right(90)

    
    def bit_itself(self):
        for node in self.snake[1:]:
            if self.head.distance(node.pos()) < 10:
                return True
            