import time
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


# creating the paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


# moving the paddles
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


# creating a ball
ball = Ball()

r_scoreboard = Scoreboard((50, 200))
l_scoreboard = Scoreboard((-50, 200))


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move(r_paddle, l_paddle, r_scoreboard, l_scoreboard)

    if ball.xcor() > 380 or ball.xcor() < -380:
        game_is_on = False
        l_scoreboard.game_over()



screen.exitonclick()