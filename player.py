import turtle as t
import Constants

class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("dark green")
        self.setheading(90)
        self.penup()
        self.refresh()

    def move(self):
        self.forward(Constants.MOVE_DISTANCE)
        

    def refresh(self):
        self.goto(Constants.PLAYER_POSITION)