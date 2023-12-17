import turtle as t
import time
from player import Player
import Constants
from scoreBoard import ScoreBoard
from car_manager import Cars


t.colormode(255)

#Screen setup
screen = t.Screen()
screen.tracer(0)
screen.setup(width=Constants.SCREEN_WIDTH,height=Constants.SCREEN_HEIGHT)
screen.listen()
screen.title(Constants.GAME_TITLE)




#Torry - the player 
Torry_The_Player = Player()
is_game_on=True

screen.onkey(key="Up",fun=Torry_The_Player.move)

score = ScoreBoard()

car = Cars()

while is_game_on:
    time.sleep(0.1)
    screen.update()
    car.random_car_gen()
    car.move_cars()

    if Torry_The_Player.ycor()>290:
        Torry_The_Player.refresh()
        score.LevelUp()
        car.increase_car_speed()
    
    for each_car in car.all_cars:
        if each_car.distance(Torry_The_Player)<27:
            score.GameOver()
            is_game_on=False
    

screen.exitonclick()