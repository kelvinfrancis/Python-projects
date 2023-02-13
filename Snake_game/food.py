from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()  # Calling the init of Trutle
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-200, 200)
        randow_y = random.randint(-200, 200)
        self.goto(random_x, randow_y)
