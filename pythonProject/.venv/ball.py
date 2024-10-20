from turtle import Turtle

class Ball(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.goto(pos)
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def collision_with_wall(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            return True
        else:
            return False

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()