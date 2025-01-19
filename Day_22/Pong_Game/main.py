from turtle import Screen, Turtle
import global_variables
from paddle import Paddle
from ball import Ball
import time


def create_screen():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=global_variables.WIDTH, height=global_variables.HEIGHT)
    screen.title(global_variables.GAME_TITLE)
    screen.tracer(0)
    return screen

def screen_listen(screen):
    screen.listen()
    screen.onkeypress(l_paddle.go_up, global_variables.UP_1)
    screen.onkeypress(l_paddle.go_down, global_variables.DOWN_1)
    screen.onkeypress(r_paddle.go_up, global_variables.UP_2)
    screen.onkeypress(r_paddle.go_down, global_variables.DOWN_2)





game_is_on = True


screen = create_screen()
#paddles = Paddle()
r_paddle =Paddle(1)
l_paddle = Paddle(-1)
screen_listen(screen)

ball = Ball()





while True:
    time.sleep(0.05)
    screen.update()

    if not(ball.ycor() in range(int(-(global_variables.HEIGHT/2 - 20)), int(global_variables.HEIGHT/2 - 20))):
        ball.bounce_horizontal()
    # if not(ball.xcor() in range(int(-(global_variables.WIDTH/2 - 20)), int(global_variables.WIDTH/2 - 20))):
    #     ball.bounce_vertical()
    
    # detect collision with paddle
    if ball.distance(r_paddle) < 40 and ball.xcor() < global_variables.WIDTH/2 - 20:
        ball.bounce_vertical()
    if ball.distance(l_paddle) < 40 and ball.xcor() > -(global_variables.WIDTH/2 - 20):
        ball.bounce_vertical()

    if ball.xcor() > global_variables.WIDTH/2 - 50:
        ball.reset_position()

    ball.move()
#exit game
screen.exitonclick()