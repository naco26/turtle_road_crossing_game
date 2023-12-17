import turtle as t
import Constants


class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(Constants.LEVEL_COLOR)
        self.goto(Constants.LEVEL_POSITION)
        self.level=1
        self.writeLevel()

    def writeLevel(self):
        self.clear()
        self.write(f"Level - {self.level}",font=Constants.FONT)

    def LevelUp(self):
        self.level+=1
        self.writeLevel()
        
    def GameOver(self):
        self.goto(Constants.GAME_OVER_POS)
        self.write("Game Over!!",font=Constants.FONT)