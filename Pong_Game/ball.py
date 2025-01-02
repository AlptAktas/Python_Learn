from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self, shape = "square", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.shapesize(1, 1)
        self.x_move = random.randrange(-15, 15, 3)
        self.y_move = random.randrange(-15, 15, 3)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_horizontal(self):
        self.y_move *= -1

    def bounce_vertical(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)