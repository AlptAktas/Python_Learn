from turtle import Screen
import time 
import snake
from food import Food
from scoreboard import Scoreboard
from globals import WIDTH, HEIGHT, SLEEP_TIMER, UP, DOWN, LEFT, RIGHT, BACKGROUND_COLOR, GAME_TITLE



class SnakeGame:
    
    def __init__(self):
        self.game_is_on = True

        self.screen = Screen()
        self.create_screen()

        self.snake = snake.Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()

        self.screen_listen()

        self.start_game()

    def create_screen(self):
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.bgcolor(BACKGROUND_COLOR)
        self.screen.title(GAME_TITLE)
        self.screen.tracer(0)


    def screen_listen(self):
        self.screen.listen()
        self.screen.onkey(self.snake.up, UP)
        self.screen.onkey(self.snake.down, DOWN)    
        self.screen.onkey(self.snake.left, LEFT)
        self.screen.onkey(self.snake.right, RIGHT)


    def collision_with_food(self):
        """Detect collision with food"""
        if self.snake.head.distance(self.food) < 10:
            self.food.refresh()
            self.snake.extend()
            self.scoreboard.increase_score()

    def collision_with_wall(self):
        """Detect collision with wall"""
        if self.snake.head.xcor() > (WIDTH/2 - 10) or self.snake.head.xcor() < -(WIDTH/2 - 10) or self.snake.head.ycor() > (HEIGHT/2 - 10) or self.snake.head.ycor() < -(HEIGHT/2 - 10):
            self.game_is_on = False
            self.scoreboard.game_over()

    
    def collision_with_tail(self):
        """Detect collision with tail"""
        for segment in self.snake.segments[1:]:
            if self.snake.head.distance(segment)/2 < 1: 
                self.game_is_on = False
                self.scoreboard.game_over() 



    def start_game(self):
        while self.game_is_on:
            

            self.collision_with_food()
            self.collision_with_wall()
            self.collision_with_tail()

            self.screen.update()
            time.sleep(SLEEP_TIMER)
            
            self.snake.move()






game = SnakeGame()




# exit game
game.screen.exitonclick()