import turtle as t
import Constants
import random

class Cars(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed=Constants.CAR_MOVE_DISTANCE
        self.all_cars=[]

    def random_car_gen(self):
        car_gen = random.randint(1,6)
        if car_gen==1:
            new_car = t.Turtle(shape="square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            Y_cor = random.randint(Constants.CAR_lOWER_LIMIT,Constants.CAR_UPPER_LIMIT)
            new_car.goto(300,Y_cor)
            new_car.color(self.random_color_gen())
            self.all_cars.append(new_car)


    def random_color_gen(self):
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        
    def increase_car_speed(self):
        self.car_speed+=Constants.CAR_INCREASE_SPEED
    
