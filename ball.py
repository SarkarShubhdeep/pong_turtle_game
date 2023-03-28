from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed('normal')
        self.y_direction = 10
        self.x_direction = 10

    def move(self, r_paddle, l_paddle, r_scoreboard, l_scoreboard):
        # print(self.ycor())

        # checking if ball is going out of Y coordinates (top & bottom) and then changing it if required
        self.change_y_direction()

        # checking if ball is hitting the paddles and bouncing it back
        self.change_x_direction(r_paddle, l_paddle, r_scoreboard, l_scoreboard)




        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)


    def change_y_direction(self):
        if self.ycor() > 280 or self.ycor() < -280:
            # print("bouncing off Y wall")
            self.y_direction = self.y_direction * -1

    def change_x_direction(self, r_paddle, l_paddle, r_scoreboard, l_scoreboard):
        # print(self.distance(r_paddle))
        if self.distance(r_paddle) < 30:
            self.x_direction = self.x_direction * -1
            r_scoreboard.increase_score()

        elif self.distance(l_paddle) < 30:
            self.x_direction = self.x_direction * -1
            l_scoreboard.increase_score()



