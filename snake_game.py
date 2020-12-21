from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WIDTH = 600
HEIGHT = 600
EPSILON = 15
SNAKE_BORDER = 280
EPSILON_FOOD = 15
EPSILON_TAIL = 9.8
LEVELS_FOR_SPEED = 3

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

food = Food()
board = Scoreboard()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.collide_turtle(food, EPSILON_FOOD):
        food.new_location()
        board.increase_level()
        snake.expand()
        if board.level % LEVELS_FOR_SPEED == 0:
            snake.speed_up()
    if snake.out_of_border(SNAKE_BORDER) or snake.collide_tail(EPSILON_TAIL):
        game_on = False
        board.game_over()


screen.exitonclick()
