from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self, shape = "square", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.all_cars = []
        self.hideturtle()
        self.speed = STARTING_MOVE_DISTANCE
        
        
    def create_cars(self):
        rand_create_change = random.randint(1, round(60/self.speed))
        if rand_create_change == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, random.randrange(-240, 280, 20))
            self.all_cars.append(new_car)
        


    def starting_position(car):
        car.goto(300, random.randrange(-240, 280, 10))

    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.speed
            car.goto(new_x, car.ycor())

    def speed_up(self):
            self.speed += MOVE_INCREMENT

