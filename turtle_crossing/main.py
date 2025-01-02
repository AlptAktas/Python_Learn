import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

WIDTH, HEIGHT = 600, 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


    
    if player.ycor() > HEIGHT/2 - 20:
        scoreboard.increase_score()
        player.starting_point()
        car_manager.speed_up()
        

screen.exitonclick()