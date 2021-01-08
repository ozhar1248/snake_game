from turtle import Turtle

SIZE_SQUARE = 20
STEP = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
NUM_TURTLES_INIT = 3


class Snake:
    def __init__(self):
        self.turtles = []
        self.add_turtle((0, 0), 1)
        self.head = self.turtles[0]
        for i in range(1, NUM_TURTLES_INIT):
            self.expand()

    def add_turtle(self, position, speed):
        turtle = Turtle()
        turtle.shape("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        turtle.speed(speed)
        self.turtles.append(turtle)

    def move(self):
        num_turtles = len(self.turtles)
        for i in range(num_turtles - 1, 0, -1):
            self.turtles[i].goto(self.turtles[i - 1].xcor(), self.turtles[i - 1].ycor())
        self.head.forward(STEP)

    def expand(self):
        position = self.turtles[-1].position()
        speed = self.turtles[-1].speed()
        self.add_turtle(position, speed)

    def out_of_border(self, border):
        x = self.head.xcor()
        y = self.head.ycor()
        return x < (-1)*border or x > border or y < (-1)*border or y > border

    def collide_turtle(self, trt, epsilon):
        return self.head.distance(trt) < epsilon

    def collide_tail(self, epsilon):
        for turtle in self.turtles[1:]:
            if self.collide_turtle(turtle, epsilon):
                return True
        return False

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        self.head.setheading(RIGHT)

    def left(self):
        self.head.setheading(LEFT)

    def reset(self, position):
        for turtle in self.turtles:
            turtle.goto(position)
        self.__init__()
