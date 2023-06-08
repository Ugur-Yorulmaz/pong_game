from turtle import Turtle, Screen
import time
# from main import Screen


class Paddle(Turtle):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(pos_x,pos_y)



    def up(self):
        self.goto(self.xcor(),self.ycor()+20)

    def down(self):
        self.goto(self.xcor(),self.ycor()-20)

