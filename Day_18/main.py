# turtle and Graphical User Interface

from turtle import Turtle, Screen, colormode
import random


direction = [0, 90, 180, 270]

tim = Turtle()
colormode(255)

tim.pensize(15)
tim.speed("fastest")

# for angle in range(3, 8):
#     for _ in range(angle):
#         tim.forward(100)
#         tim.right(360/angle)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# screen = Screen()
# screen.exitonclick()

for _  in range(200):
    tim.forward(30)
    tim.setheading(random.choice(direction))
    tim.pencolor(random_color())


