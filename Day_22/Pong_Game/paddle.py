from turtle import Turtle 
import global_variables


class Paddle(Turtle):

    def __init__(self, paddle_orient, shape = "square", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(paddle_orient*((global_variables.WIDTH/2)-50), 0)

    
    def go_up(self, paddle_num=0):
        new_y = self.ycor() + global_variables.PADDLE_STEP
        if new_y < global_variables.HEIGHT/2 - 36:
            self.goto(self.xcor(), new_y)


    def go_down(self, paddle_num=0):
        new_y = self.ycor() - global_variables.PADDLE_STEP
        if new_y > -(global_variables.HEIGHT/2 - 48):
            self.goto(self.xcor(), new_y)
        


    
    
