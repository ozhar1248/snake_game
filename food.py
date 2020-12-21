from turtle import Turtle
import random

BORDER = 280


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.penup()
        self.new_location()

    def new_location(self):
        self.goto(random.randint((-1)*BORDER, BORDER), random.randint((-1)*BORDER, BORDER))
