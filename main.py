from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

scoreboard=Scoreboard()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

right_paddle=Paddle(380,0)
left_paddle=Paddle(-380,0)
ball=Ball()
screen.update()

screen.listen()
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")
speed=0.1
game_is_on=True
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()
    # Bouncing the ball
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce()

    # Bouncing from Paddle
    if (ball.xcor()>360 and ball.distance(right_paddle)<50 or ball.xcor()<-360 and ball.distance(left_paddle)<50):
    # if (ball.xcor()>360 and abs(ball.ycor()-(right_paddle.ycor())<27) or (ball.xcor()<-360 and abs(ball.ycor()-left_paddle.ycor())<27)):
        print("ball.ycor()-(left_paddle.ycor()<23",abs(ball.ycor()-left_paddle.ycor())<23)
        print("left_paddle.ycor()-ball.ycor()<23",abs(left_paddle.ycor()-ball.ycor())<23)
        print("ball.ycor()",ball.ycor())
        print("left_paddle.ycor()",left_paddle.ycor())
        if speed<=0:
            speed=0.01
        else:
            speed-=0.03
        ball.paddle_return()

    if ball.xcor()>363:
        ball.out_of_bound()
        scoreboard.score_left()
        speed=0.1

    if ball.xcor()<-363:
        ball.out_of_bound()
        scoreboard.score_right()
        speed=0.1













screen.exitonclick()
