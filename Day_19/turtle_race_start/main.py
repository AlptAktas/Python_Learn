from turtle import Turtle, Screen
import random


class TurtleGame:

    colours = ["red", "orange", "yellow", "green", "blue", "purple", "black", "gray"]
    turtles = []
    width, height = 500, 400
    screen = Screen()
    

    def __init__(self):

        self.screen.setup(width=self.width, height=self.height)

        for i in self.colours:
            tr = Turtle(shape="turtle")
            tr.penup()
            tr.color(i)
            self.turtles.append(tr)


    def place_turtles_to_startpoint(self):

        placement_height_per_turtle = self.height / (len(self.turtles))
        placement_height = self.height + placement_height_per_turtle
        for tr in self.turtles:
            tr.goto(x=-(self.width/2 - 20), y=placement_height/2 - placement_height_per_turtle)
            placement_height -= placement_height_per_turtle * 2


game = TurtleGame()


user_bet = game.screen.textinput(title="Make your bet", prompt="Which turtje will win the race? Enter a color: ")

game.place_turtles_to_startpoint()

is_game_on = True


while is_game_on:
    for turtle in game.turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() > game.width / 2 - 20:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You'be won! The {winning_color} turtle is the winner!")
            else:
                print(f"You'be lost! The {winning_color} turtle is the winner!")
            is_game_on = False
            break




game.screen.exitonclick()