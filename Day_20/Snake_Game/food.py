from turtle import Turtle
import random
from globals import WIDTH, HEIGHT


class Food(Turtle):


    def __init__(self, shape = "circle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)

        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()



    def refresh(self):
        random_x = random.randrange(-(WIDTH/2 - 20), (WIDTH/2 - 20), 20)
        random_y = random.randrange(-(HEIGHT/2 - 20), (HEIGHT/2 - 20), 20)
        self.goto(random_x, random_y)


