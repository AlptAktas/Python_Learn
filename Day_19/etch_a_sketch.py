from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(turn_right, "d")
screen.onkey(move_backward, "s")
screen.onkey(clear, "c")

screen.exitonclick()
