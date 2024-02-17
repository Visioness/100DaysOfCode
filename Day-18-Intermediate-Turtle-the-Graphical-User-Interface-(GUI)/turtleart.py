import turtle as t
import random
import colorgram

turtle = t.Turtle()
t.colormode(255)

def main():
    # Dashed line
    """turtle.hideturtle()
    turtle.shape("turtle")
    turtle.penup()
    turtle.setpos(-300, -300)
    interval = 50
    turtle.speed(1)
    for i in range(4):
        for i in range(int(500 / interval)):
            turtle.pencolor(random.choice(["blue", "red", "yellow", "green"]))
            turtle.pendown()
            turtle.forward(interval / 2)
            turtle.penup()
            turtle.forward(interval / 2)
            
        turtle.left(90)"""
    
    # Polygons with different colors
    """turtle.shape("turtle")
    turtle.speed(3)
    colors = ["red", "yellow", "blue", "purple", "green", "black", "brown", "orange"]
    setstart(-100, 400)
    number_of_sides = 3
    while number_of_sides < 11:
        turtle.pencolor(colors.pop(0))
        for i in range(number_of_sides):
            turtle.forward(100)
            turtle.right(360 / number_of_sides)
        number_of_sides += 1"""
    
    # Random Walk
    """turtle.speed(5)
    turtle.pensize(10)
    colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    for i in range(200):
        turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.setheading(random.choice([0, 90, 180, 270]))
        turtle.forward(20)"""
    
    # Spirograph
    """turtle.speed("fastest")
    turtle.pensize(1)
    angle = 5
    for i in range(int(360 / angle)):
        turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        turtle.circle(100)
        turtle.setheading(turtle.heading() + angle)"""
    
    # Colorgram / getting colors from image
    """colors = colorgram.extract("hirstcolors.jpg", 30)
    colorlist = []
    for color in colors:
        colorlist.append((color.rgb.r, color.rgb.g, color.rgb.b))
    print(colorlist)"""
    colorlist = [(206, 161, 82), (55, 88, 129), (142, 91, 41), (221, 207, 107), 
                 (138, 26, 48), (133, 175, 200), (157, 47, 84), (46, 55, 102), 
                 (169, 159, 41), (131, 188, 145), (82, 20, 43), (36, 43, 68), 
                 (186, 93, 106), (189, 139, 163), (87, 115, 177), (87, 156, 97), 
                 (59, 39, 33), (79, 154, 165), (196, 81, 71), (54, 128, 122), 
                 (45, 73, 76), (162, 202, 216), (44, 75, 73), (78, 76, 45), 
                 (167, 207, 165), (219, 175, 187)]
    
    # Drawing 10x10 hirst spot painting
    """turtle.speed(0)
    setstart(-400, -300)
    start = turtle.position()
    interval = 60
    repeat = 10
    turtle.hideturtle()
    turtle.penup()
    for i in range(repeat):
        for j in range(repeat):
            turtle.dot(30, random.choice(colorlist))
            if j != 9:
                turtle.forward(interval)

        if i != 9:
            turtle.sety(turtle.position()[1] + interval)
            turtle.setx(start[0])"""
    
    turtle.speed(0)
    setstart(0, -350)
    turtle.left(90)
    branch(120)

def branch(length):
    if length < 10:
        return
    else:
        turtle.forward(length)
        turtle.setheading(turtle.heading() - 30)
        branch(3 * length / 4)
        turtle.setheading(turtle.heading() + 60)
        branch(3 * length / 4)
        turtle.setheading(turtle.heading() - 30)
        turtle.backward(length)


def setstart(xpos, ypos):
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(xpos, ypos)
    turtle.showturtle()
    turtle.pendown()


if __name__ == "__main__":
    main()

screen = t.Screen()
screen.exitonclick()