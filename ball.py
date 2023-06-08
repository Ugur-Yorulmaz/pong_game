from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.inc_y=20
        self.inc_x=10

    def move(self):
        next_x=self.xcor()+self.inc_x
        next_y=self.ycor()+self.inc_y
        self.goto(next_x,next_y)

    def bounce(self):
        self.inc_y*=-1
        self.move()

    def paddle_return(self):
        self.inc_x*=-1
        self.move()

    def out_of_bound(self):
        self.goto(0,0)
        self.inc_x*=-1

    # def speed_up(self):





